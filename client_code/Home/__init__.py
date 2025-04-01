from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.homeLink.role='selected'

  def appointment_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Citas')

  def duty_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def reports_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def statistics_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('stats')

