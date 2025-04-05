from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import window


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.reports_link.enabled = False
    self.reports_link_copy.enabled = False
    self.statistics_link.enabled = False
    self.statistics_link_copy.enabled = False 
    self.appointment_link.enabled = False
    self.appointment_link_copy.enabled = False    

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.homeLink.role='selected'
    if window.innerHeight > window.innerWidth:
      self.phone_panel.visible = True
      self.pc_panel.visible = False
      
      self.appointments_image_small.height = window.innerWidth/2
      self.stats_image.height_small = window.innerWidth/2
      self.reports_image.height_small = window.innerWidth/2
      self.duty_image.height_small = window.innerWidth/2
      
    else:
      self.phone_panel.visible = False
      self.pc_panel.visible = True

      self.appointments_image.height = window.innerWidth/5
      self.stats_image.height = window.innerWidth/5
      self.reports_image.height = window.innerWidth/5
      self.duty_image.height = window.innerWidth/5

  def appointment_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Appointments')

  def duty_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Duty')

  def reports_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def statistics_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('stats')

