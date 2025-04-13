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
from anvil.js import window
from datetime import datetime, timedelta


class createAppointment(createAppointmentTemplate):
  def __init__(self, cita=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #types = self.getRequest()
    #print(types)
    self.types = self.appointment_types_get_all()
    self.type_dropdown.items = [type["name"] for type in self.types]
    self.lbl_money.text = str(self.find_money())
    self.startTime = datetime.now()
    self.cita = cita

    if window.innerHeight > window.innerWidth:
      self.phone_panel.visible = True
      self.pc_panel.visible = False
      self.fill_phone_content()
    else:
      self.phone_panel.visible = False
      self.pc_panel.visible = True
      self.fill_pc_content()


  def save_button_click(self, **event_args):
    if self.cita:
      # Llamar al endpoint de editar la información
      open_form('Appointments')
    else:
      appt = {
        "doctor": "76bf31f8-538a-4d99-8d45-26f5d39528fb",
        "idPrv": self.id_input.text,
        "type": self.find_type_id(),
        "comment": self.description_input.text,
        "meds": self.meds_input.text,
        "startDate": self.startTime.isoformat(),
        "endDate": datetime.now().isoformat()
      }
      created = anvil.server.call("create_appointment", appt)
      print(created)
      open_form('Appointments')      

  def discard_button_click(self, **event_args):
    open_form('Appointments')

  def type_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.lbl_money.text = str(self.find_money())
    self.lbl_money_copy.text = str(self.find_money())

  def appointment_types_get_all(self):
    return anvil.server.call("get_all_appointment_types")["content"]
  
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    elapsed_time = datetime.now() - self.startTime  # Tiempo transcurrido en segundos
    elapsed_minutes = elapsed_time.seconds // 60  # Obtiene los minutos
    elapsed_seconds = elapsed_time.seconds % 60   # Obtiene los segundos restantes
    
    # Formatea MM:SS con ceros a la izquierda
    self.appointment_timer.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"
    self.appointment_timer_copy.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"

  def id_input_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.id_input.text = "" if "cita" in self.id_input.text else self.id_input.text
    self.id_input_copy.text = "" if "cita" in self.id_input.text else self.id_input.text

  def description_input_focus(self, **event_args):
    """This method is called when the text area gets focus"""
    self.description_input.text = "" if "Notas" == self.description_input.text else self.description_input.text
    self.description_input_copy.text = "" if "Notas" == self.description_input.text else self.description_input.text

  def meds_input_focus(self, **event_args):
    """This method is called when the text area gets focus"""
    self.meds_input.text = "" if "Medicamentos" == self.meds_input.text else self.meds_input.text
    self.meds_input_copy.text = "" if "Medicamentos" == self.meds_input.text else self.meds_input.text

  def find_money(self):
    return [type["value"] for type in self.types if type["name"] == self.type_dropdown.selected_value][0]
    
  def find_type_id(self):
    print(self.types)
    return [type["id"] for type in self.types if type["name"] == self.type_dropdown.selected_value][0]

  def fill_phone_content(self):
    if self.cita:
      # Rellenar los campos con los datos existentes
      self.create_form_title.text = "Editar cita"
      self.id_input.text = str(self.cita.get('name', ''))
      self.description_input.text = self.cita.get('notes', '')
      self.meds_input.text = self.cita.get('medicamentos', '')
      self.type_dropdown.selected_value = self.cita.get('type', 'Normal')
      self.meds_input.text = self.cita.get('meds', 'Therearenomeds')      
      self.lbl_money.text = str(self.find_money())
    
    
  def fill_pc_content(self):
    if self.cita:
      # Rellenar los campos con los datos existentes
      self.create_form_title.text = "Editar cita"
      self.id_input_copy.text = str(self.cita.get('name', ''))
      self.description_input_copy.text = self.cita.get('notes', '')
      self.meds_input_copy.text = self.cita.get('medicamentos', '')
      self.type_dropdown_copy.selected_value = self.cita.get('type', 'Normal')
      self.meds_input_copy.text = self.cita.get('meds', 'Therearenomeds')      
      self.lbl_money_copy.text = str(self.find_money())




