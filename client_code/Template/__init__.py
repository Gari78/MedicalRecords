from ._anvil_designer import TemplateTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
from anvil import js
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Template(TemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def appointmentsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Appointments')

  def statisticsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('stats')

  def reportsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def reset_links(self, **event_args):
    self.homeLink.role = ''
    self.statisticsLink.role = ''
    self.appointmentsLink.role = ''
    self.reportsLink.role = ''

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def dutyLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Duty')

