from ._anvil_designer import AppointmentsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Appointments(AppointmentsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.data = self.appointments_get_all()

    self.AppointmentListPanel.items = self.data

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.appointmentsLink.role = 'selected'
    #response = await fetch("https://api.tuservicio.com/endpoint");

  def addAppointmentButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    from .createAppointment import createAppointment
    popup = createAppointment()
    open_form(popup)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  def filters_button_click(self, **event_args):
    if self.init_date_picker.visible:
      self.init_date_picker.visible = False
      self.end_date_picker.visible = False
      self.type_drop_down.visible = False
      self.apply_filters.visible = False
      self.filters_button.text = "Filtros"
    else:
      self.init_date_picker.visible = True
      self.end_date_picker.visible = True
      self.type_drop_down.visible = True
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
      fields = [item['notes'], item['name'], item['type']]
      if any(find in field.lower() for field in fields):
          auxdata.append(item)
    self.AppointmentListPanel.items = auxdata

  def appointments_get_all(self):
    return anvil.server.call("get_all_appointments")["content"]
    
      
    
    
    
    