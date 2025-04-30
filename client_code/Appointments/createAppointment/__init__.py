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
      appt = {
        "idPrv": self.id_input.text,
        "type": self.find_type_id(),
        "comment": self.description_input.text,
        "meds": self.meds_input.text,
      }
      updated = anvil.server.call("update_appointment", appt, self.cita.get("id", 0))
    else:
      appt = {
        "idPrv": self.id_input.text,
        "type": self.find_type_id(),
        "comment": self.description_input.text,
        "meds": self.meds_input.text,
        "initDate": self.startTime.isoformat().replace(" ","T"),
        "endDate": datetime.now().isoformat().replace(" ","T")
      }
      created = anvil.server.call("create_appointment", appt)
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
    if not self.cita:
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
    return [type["id"] for type in self.types if type["name"] == self.type_dropdown.selected_value][0]

  def fill_pc_content(self):
    if self.cita:
      self.create_form_title.text = "Editar cita"
      self.id_input.text = self.cita.get("idPrv", "jeje")
      self.description_input.text = self.cita.get("comment", "miau")
      self.type_dropdown.selected_value = f"{self.cita.get('type', 'miau').get('name', '')}"
      self.meds_input.text = self.cita.get('meds', 'Therearenomeds')      
      self.lbl_money.text = f"{self.cita.get('type', 'miau').get('value',0)}€"
      timelapse = datetime.fromisoformat(self.cita.get('endDate', 'miau').replace("Z","")) - datetime.fromisoformat(self.cita.get('initDate', 'miau').replace("Z",""))
      elapsed_minutes = timelapse.seconds // 60
      elapsed_seconds = timelapse.seconds % 60 
      self.appointment_timer.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"
    
    
  def fill_phone_content(self):
    if self.cita:
      self.create_form_title.text = "Editar cita"
      self.id_input_copy.text = self.cita.get("idPrv", "jeje")
      self.description_input_copy.text = self.cita.get("comment", "miau")
      self.type_dropdown_copy.selected_value = f"{self.cita.get('type', 'miau').get('name', '')}"
      self.meds_input_copy.text = self.cita.get('meds', 'Therearenomeds')      
      self.lbl_money_copy.text = f"{self.cita.get('type', 'miau').get('value',0)}€"
      timelapse = datetime.fromisoformat(self.cita.get('endDate', 'miau').replace("Z","")) - datetime.fromisoformat(self.cita.get('initDate', 'miau').replace("Z",""))
      elapsed_minutes = timelapse.seconds // 60
      elapsed_seconds = timelapse.seconds % 60 
      self.appointment_timer_copy.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"

