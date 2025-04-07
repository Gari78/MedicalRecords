from ._anvil_designer import createAppointmentTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
import anvil.http


class createAppointment(createAppointmentTemplate):
  def __init__(self, cita=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #types = self.getRequest()
    #print(types)
    self.type_dropdown.items = ["Normal", "Telemático", "Urgente", "Privado"]
    self.startTime = int(time.time())

    self.cita = cita  # Guardamos la cita por si es una edición

    if self.cita:
      # Rellenar los campos con los datos existentes
      self.id_input.text = str(cita.get('nombre', ''))
      self.description_input.text = cita.get('descripcion', '')
      self.meds_input.text = cita.get('medicamentos', '')
      self.type_dropdown.selected_value = cita.get('tipo', 'Normal')

  def save_button_click(self, **event_args):
    if self.cita:
      # Llamar al endpoint de editar la información
      open_form('Appointments')
    else:
      open_form('Appointments')      

  def discard_button_click(self, **event_args):
    open_form('Appointments')

  def type_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    elapsed_time = int(time.time()) - self.startTime  # Tiempo transcurrido en segundos
    elapsed_minutes = elapsed_time // 60  # Obtiene los minutos
    elapsed_seconds = elapsed_time % 60   # Obtiene los segundos restantes
    
    # Formatea MM:SS con ceros a la izquierda
    self.appointment_timer.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"

  def getRequest(self):
    token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4SU9OdS1tQnlpN2N3TmpoNUlTOXdzLXdyRm83NXBVMEhfRWQyOVladkQ4In0.eyJleHAiOjE3NDI3ODk4NDQsImlhdCI6MTc0Mjc1Mzg0NCwianRpIjoiM2YwNDAyMjItNTc1Yi00NmQ3LWFhOTAtY2EyMmU1NTQyZWE2IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9NZWRpY2FsUmVjb3JkcyIsImF1ZCI6InJlYWxtLW1hbmFnZW1lbnQiLCJzdWIiOiI3MDFmMjk2NS1hMTRjLTRkMjItYTJlYS1jYzI3ODVmOGQ3MDMiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJhcHAiLCJzaWQiOiIzM2I1NTA3YS1mNjFlLTQ2ZTItYWIzMS00ZjdmZWRkYWM5MzEiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJhZG1pbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1pZGVudGl0eS1wcm92aWRlcnMiLCJ2aWV3LXJlYWxtIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6ImFkbWluX3VzZXJzIiwiZW1haWwiOiJhZG1pbl91c2VyczEua2V5Y2xvYWtAc29vbG9naWMuY29tIn0.lpFMIiJ4-T5UqveKvh_hddW51lBuEofhzgEEJOX0nIcH4Gt1f2jwuV01z6XBwC1qB3cSDrYa0kLQyHIxJCeumEFvFhN7bZKMbDg0lFqinC5xU5arm77_ceJttL0NGybo3iNVFEsIxEvwdT3uJQC0QZWJKG2GwtDLnkU2x0EOgTQ8ARGCJHnFM7uEmwmsc3ANXdyQP_CoMNGRMEyTu8ojv2Rgr0MmCO7Q7QDZcFNggtbDtvKLjsim8CK2js-B7DOAf7528WDVMv8p6EbEWWNRapGck4NKIEkneGlJIgaBHynrDwnZS-i8S2mlJUQdI1DOIK8AGiThwf70h5AkHLwgww"
    headers = {
      "Authorization": f"Bearer {token}",
      "Content-Type": "application/json"
    }
    #response = anvil.http.request("http://94.248.72.87:5000/api/v1/appointment_types/", method="GET", headers=headers, json=True)
    #return response

  def id_input_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.id_input.text = "" if "cita" in self.id_input.text else self.id_input.text


  def description_input_focus(self, **event_args):
    """This method is called when the text area gets focus"""
    self.description_input.text = "" if "Notas" == self.description_input.text else self.description_input.text

  def meds_input_focus(self, **event_args):
    """This method is called when the text area gets focus"""
    self.meds_input.text = "" if "Medicamentos" == self.meds_input.text else self.meds_input.text



