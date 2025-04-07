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
      fields = [item['descripcion'], item['nombre'], item['tipo']]
      if any(find in field.lower() for field in fields):
          auxdata.append(item)
    self.AppointmentListPanel.items = auxdata

  def appointments_get_all(self):
    return [
        {"nombre": "235769dkj", "descripcion": "Le dolía el alma", "tipo": "Normal", "dinero": "7,4", "date":"01-01-2025"},
        {"nombre": "jdj532gds", "descripcion": "El bombero con dolor de abdominales", "tipo": "urgente", "dinero": "10", "date":"01-01-2025"},
        {"nombre": "jf84jdo20", "descripcion": "Zanahorio", "tipo": "privado", "dinero": "25", "date":"01-01-2025"},
        {"nombre": "8fdg73hds", "descripcion": "Gato filósofo", "tipo": "normal", "dinero": "7,4", "date":"01-01-2025"},
        {"nombre": "4jfk93kdl", "descripcion": "Un pez llamado Juan", "tipo": "privado", "dinero": "25", "date":"01-01-2025"},
        {"nombre": "0djh392fk", "descripcion": "La montaña de los sueños", "tipo": "urgente", "dinero": "10", "date":"01-01-2025"},
        {"nombre": "9gdh28sjk", "descripcion": "Mago sin varita", "tipo": "normal", "dinero": "7,4", "date":"01-01-2025"},
        {"nombre": "kl39dkf02", "descripcion": "Camino de caramelos", "tipo": "privado", "dinero": "25", "date":"01-01-2025"},
        {"nombre": "p2jfk38d9", "descripcion": "El hombre que hablaba con sombras", "tipo": "urgente", "dinero": "10", "date":"01-01-2025"},
        {"nombre": "z8fk392ld", "descripcion": "Biblioteca encantada", "tipo": "normal", "dinero": "7,4", "date":"01-01-2025"},
        {"nombre": "xj29fk30s", "descripcion": "Dragón dormilón", "tipo": "privado", "dinero": "25", "date":"01-01-2025"},
        {"nombre": "m3ldk49jf", "descripcion": "Pirata sin barco", "tipo": "urgente", "dinero": "10", "date":"01-01-2025"},
        {"nombre": "h4dk39sla", "descripcion": "Los zapatos del destino", "tipo": "normal", "dinero": "7,4", "date":"01-01-2025"}
    ]
    
      
    
    
    
    