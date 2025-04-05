from ._anvil_designer import DutyTemplate
from anvil import *
import plotly.graph_objects as go
from datetime import datetime, time
from anvil.js import window

class Duty(DutyTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.start_button.enabled = False
        self.start_button_phone.enabled = False
        self.inittime = None
        self.endtime = None
        self.total_time = 0
        self.hourmoney = 0
        self.start = False
        self.progress_label.text = "0%"
        self.progress_label_width.width = 50
          
        
    def form_show(self, **event_args):
        """This event is triggered when the form is displayed on the screen"""
        self.layout.reset_links()
        self.layout.dutyLink.role = 'selected'
        if window.innerHeight > window.innerWidth:
          self.phone_layout.visible = True
          self.pc_layout.visible = False
        else:
          self.phone_layout.visible = False
          self.pc_layout.visible = True
          
        self.progress_bar_panel.visible = False

    def timer_1_tick(self, **event_args):
      """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
      now = datetime.now()
      
      if not self.start:
        if not self.start_button.enabled and self.inittime_picker.date and self.hourmoney_input.text != "" and self.endtime_picker.date:
            self.start_button.enabled = True
        elif not self.start_button_phone.enabled and self.inittime_picker_phone.date and self.hourmoney_input_phone.text != "" and self.endtime_picker_phone.date:
            self.start_button_phone.enabled = True
      else:
        sofar = datetime.now() - self.inittime
        remaining = self.endtime - datetime.now()
        money_label = f"{sofar.total_seconds() * self.hourmoney/3600:.2f}€ ;)"
        time_left_label = self.seconds_to_timestring(remaining.total_seconds())

        if self.pc_layout.visible:
          self.timer_timer_label.text = time_left_label
          self.money_label_counter.text = money_label
          self.clock_timer_label.text = now.strftime("%H:%M:%S")
        else:
          self.timer_timer_label_phone.text = time_left_label
          self.money_label_counter_phone.text = money_label
          self.clock_timer_label_phone.text = now.strftime("%H:%M:%S")
        if self.total_time > 0:
          percentage = int(100 * sofar.total_seconds()/self.total_time)
          self.progress_label.text = f"{percentage}%"
          self.progress_label_width.width = max(50, 0.95*min(percentage*window.innerWidth/100, 0.95*window.innerWidth))

    def start_button_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.clock_card.visible = True
      self.timeleft_card.visible = True
      self.money_earned_card.visible = True
      self.progress_bar_panel.visible = True
      
      self.inittime = self.inittime_picker.date.replace(tzinfo=None)
      self.endtime = self.endtime_picker.date.replace(tzinfo=None)
      self.total_time = self.endtime - self.inittime
      self.total_time = self.total_time.total_seconds()
      self.hourmoney = float(self.hourmoney_input.text)
      self.start = True
      self.start_button.text = "Editar!"
      
    def start_button_phone_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.clock_card_phone.visible = True
      self.timeleft_card_phone.visible = True
      self.money_earned_card_phone.visible = True
      self.progress_bar_panel.visible = True
      
      self.inittime = self.inittime_picker_phone.date.replace(tzinfo=None)
      self.endtime = self.endtime_picker_phone.date.replace(tzinfo=None)
      self.total_time = self.endtime - self.inittime
      self.total_time = self.total_time.total_seconds()
      self.hourmoney = float(self.hourmoney_input_phone.text)
      self.start = True
      self.start_button_phone.text = "Editar!"

    def seconds_to_timestring(self,seconds):
      hours = int(seconds // 3600)
      minutes = int((seconds % 3600) // 60)
      seconds = int(seconds % 60)
      return(f"{hours:02}:{minutes:02}:{seconds:02}")
      
      
      
