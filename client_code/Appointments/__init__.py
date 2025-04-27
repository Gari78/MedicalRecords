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
from datetime import datetime, timedelta, timezone


class Appointments(AppointmentsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.apply_filters.enabled = False
    self.end_date_picker.date = datetime.now()
    self.init_date_picker.date = self.end_date_picker.date - timedelta(days=7)
    
    self.types = self.appointment_types_get_all()
    self.data = self.appointments_get_all()
    self.type_drop_down.items = ["Todos"] + [type["name"] for type in self.types]

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
      self.end_date_picker.date = datetime.now()
      self.init_date_picker.date = self.end_date_picker.date - timedelta(days=7)
      self.type_drop_down.selected_value = "Todos"
      self.apply_filters.text = "Aplicar"
      
    self.data = self.appointments_get_all()
    self.AppointmentListPanel.items = self.data
    
  def finder_input_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    if "Búsqueda" in self.finder_input.text:
      self.finder_input.text = ""

  def finder_input_change(self, **event_args):
    auxdata = []
    for item in self.data:
      find = self.finder_input.text.lower()
      fields = [item['comment'], item['meds'], item['type']['name'], item['idPrv']]
      if any(find in field.lower() for field in fields):
          auxdata.append(item)
    self.AppointmentListPanel.items = auxdata

  def appointments_get_all(self):
    endDate = self.end_date_picker.date.isoformat()
    initDate = self.init_date_picker.date.isoformat()
    print(self.type_drop_down.selected_value)
    type_id = [item["id"] for item in self.types if item["name"]==self.type_drop_down.selected_value]
    type_id = type_id[0] if len(type_id)==1 else None
    
    return anvil.server.call("get_all_appointments",initDate,endDate,type_id)["content"]

  def appointment_types_get_all(self):
    return anvil.server.call("get_all_appointment_types")["content"]

  def init_date_picker_change(self, **event_args):
    if self.apply_filters.enabled:
      self.data = self.appointments_get_all()
      self.AppointmentListPanel.items = self.data      
    elif self.end_date_picker.date:
        self.apply_filters.enabled = True

  def end_date_picker_change(self, **event_args):
    if self.apply_filters.enabled:
      self.data = self.appointments_get_all()
      self.AppointmentListPanel.items = self.data      
    elif self.init_date_picker.date:
        self.apply_filters.enabled = True

  def type_drop_down_change(self, **event_args):
    if self.apply_filters.enabled:
      self.data = self.appointments_get_all()
      self.AppointmentListPanel.items = self.data     
    else:
      self.apply_filters.enabled = True
    
      
    
    
    
    