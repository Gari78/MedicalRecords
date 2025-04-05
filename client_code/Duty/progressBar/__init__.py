from ._anvil_designer import ProgressBarTemplate
from anvil import *
from math import ceil

class ProgressBar(ProgressBarTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    
    self._value=properties['value']
    self._style=properties['style']
    self._border_width=properties['border_width']
    self._border_colour=properties['border_colour']
    self._bar_colour=properties['bar_colour']
    self._block_size=properties['block_size']
    self._block_gap=properties['block_gap']
    self._height=properties['height']
    
    # Set some defaults.
    if self._value is None:
      self._value = 0
    if self._style is None:
      self._style = "smooth"
    
    self.initialised = True
    self.update()
    
  ###################
  # Getters & Setters
  ###################
  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, value):
    self._height = value
    self.update()
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    self._value = value
    self.update()

  @property
  def style(self):
    return self._style
  
  @style.setter
  def style(self, value):
    if value in ["smooth", "block"]:
      self._style = value
    else:  
      self._style = "smooth"
    
    self.update()
  
  @property
  def border_width(self):
    return self._border_width
  
  @border_width.setter
  def border_width(self, value):
    if value < 0:
      value = 0
      
    self._border_width = value
    self.update()
    
  @property
  def border_colour(self):
    return self._border_colour
  
  @border_colour.setter
  def border_colour(self, value):
    self._border_colour = value
    self.update()
    
  @property
  def bar_colour(self):
    return self._bar_colour
  
  @bar_colour.setter
  def bar_colour(self, value):
    self._bar_colour = value
    self.update()
    
  @property
  def block_resolution(self):
    return self._block_resolution
  
  @block_resolution.setter
  def block_resolution(self, value):
    self._block_resolution = value
    self.update()
    
  @property
  def block_gap(self):
    return self._block_gap
  
  @block_gap.setter
  def block_gap(self, value):
    self._block_gap = int(value)
    self.update()
    
  #########################  
  # Getters & Setters END #
  #########################
    
  def update(self, **event_args):
    try:
      self.initialised = not self.initialised
    except:
      return
    
    self.canvas_1.height = self._height
    
    if self._style == "smooth":
      self.update_smooth()
    elif self._style == "block":
      self.update_block()
      
  def update_block(self, **args):
    c = self.canvas_1
    c.fill_style = self._bar_colour
    self.clear_progress()

    bar_width = c.get_width()/100. * self._value

    # Block resolution is how many % each block is. 
    # Make block width proportional in pixels to block size.
    block_width = c.get_width()/100. * self._block_size
    
    # Number of blocks is int(bar width / block size)
    blocks=bar_width / block_width
    if self.value == 100:
      blocks += 1
    block_pos = 0
    for i in range(int(blocks)):
      c.fill_rect(self.border_width + (block_width*i), self.border_width, block_width - self._block_gap, c.get_height() - (self.border_width*2))
      
    self.draw_border()
    
  def update_smooth(self, **args):
    c = self.canvas_1
    self.clear_progress()

    bar_width = int(c.get_width()/100. * self._value)

    c.fill_style = self._bar_colour
    c.fill_rect(0, 0, bar_width, c.get_height())
    self.draw_border()
    c.stroke()
    
  def form_show(self, **event_args):
    self.prepare_canvas()
    self.update()

  def prepare_canvas(self, **args):
      self.draw_border()
    
  def clear_progress(self, **args):
    c = self.canvas_1
    c.clear_rect(0, 0, c.get_width(), c.get_height())
    
  def draw_border(self, **args):
    if self._border_width > 0:
      c = self.canvas_1
      
      # See here for why this is necessary : http://diveintohtml5.info/canvas.html#pixel-madness
      if self._border_width % 2 == 0:
        adjustment = 0.5
      else:
        adjustment = 0.0
        
      old_width = c.line_width
      c.line_width = self._border_width
      c.stroke_style = self._border_colour
      c.stroke_rect((c.line_width/2.0) + adjustment, (c.line_width/2.0) + adjustment, c.get_width() - (c.line_width) - 1, c.get_height() - (c.line_width))
      c.line_width = old_width
