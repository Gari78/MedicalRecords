from ._anvil_designer import reportsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class reports(reportsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.apply_filters.enabled = False
    self.data = self.reports_get_all()

    self.reportsPanel.items = self.data

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.reportsLink.role = "selected"
    # response = await fetch("https://api.tuservicio.com/endpoint");

  def createReportButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    from .createReport import createReport

    popup = createReport()
    open_form(popup)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  def filters_button_click(self, **event_args):
    if self.init_date_picker.visible:
      self.init_date_picker.visible = False
      self.end_date_picker.visible = False
      self.apply_filters.visible = False
      self.filters_button.text = "Filtros"
    else:
      self.init_date_picker.visible = True
      self.end_date_picker.visible = True
      self.apply_filters.visible = True
      self.filters_button.text = "Ocultar"

  def apply_filters_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.apply_filters.text == "Aplicar":
      self.apply_filters.text = "Quitar"
    else:
      self.apply_filters.text = "Aplicar"

  def finder_input_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    if "Búsqueda" in self.finder_input.text:
      self.finder_input.text = ""

  def finder_input_change(self, **event_args):
    auxdata = []
    for item in self.data:
      find = self.finder_input.text.lower()
      fields = [str(item["income"]["gross"]), str(item["income"]["net"]), str(item["patients"]["total"]["quantity"])]
      if any(find in field.lower() for field in fields):
        auxdata.append(item)
    self.reportsPanel.items = auxdata

  def reports_get_all(self):
    return anvil.server.call("get_all_reports")["content"]

  def init_date_picker_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.end_date_picker.date:
      self.apply_filters.enabled = True

  def end_date_picker_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.init_date_picker.date:
      self.apply_filters.enabled = True
