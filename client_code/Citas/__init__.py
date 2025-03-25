from ._anvil_designer import CitasTemplate
from anvil import *
import anvil
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Citas(CitasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    data = [
        {"nombre": "235769dkj", "descripcion": "Le dolía el alma", "tipo": "normal", "dinero": "7,4"},
        {"nombre": "jdj532gds", "descripcion": "El bombero con dolor de abdominales", "tipo": "urgente", "dinero": "10"},
        {"nombre": "jf84jdo20", "descripcion": "Zanahorio", "tipo": "privado", "dinero": "25"},
        {"nombre": "8fdg73hds", "descripcion": "Gato filósofo", "tipo": "normal", "dinero": "7,4"},
        {"nombre": "4jfk93kdl", "descripcion": "Un pez llamado Juan", "tipo": "privado", "dinero": "25"},
        {"nombre": "0djh392fk", "descripcion": "La montaña de los sueños", "tipo": "urgente", "dinero": "10"},
        {"nombre": "9gdh28sjk", "descripcion": "Mago sin varita", "tipo": "normal", "dinero": "7,4"},
        {"nombre": "kl39dkf02", "descripcion": "Camino de caramelos", "tipo": "privado", "dinero": "25"},
        {"nombre": "p2jfk38d9", "descripcion": "El hombre que hablaba con sombras", "tipo": "urgente", "dinero": "10"},
        {"nombre": "z8fk392ld", "descripcion": "Biblioteca encantada", "tipo": "normal", "dinero": "7,4"},
        {"nombre": "xj29fk30s", "descripcion": "Dragón dormilón", "tipo": "privado", "dinero": "25"},
        {"nombre": "m3ldk49jf", "descripcion": "Pirata sin barco", "tipo": "urgente", "dinero": "10"},
        {"nombre": "h4dk39sla", "descripcion": "Los zapatos del destino", "tipo": "normal", "dinero": "7,4"}
    ]

    self.AppointmentListPanel.items = data

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.appointmentsLink.role = 'selected'
    #response = await fetch("https://api.tuservicio.com/endpoint");

  def addAppointmentButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..createAppointment import createAppointment
    popup = createAppointment()
    open_form(popup)
    
    