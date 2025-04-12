from ._anvil_designer import AppointmentListTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import window


class AppointmentList(AppointmentListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.item:
      if window.innerHeight > window.innerWidth:
        self.phone_panel.visible = True
        self.pc_panel.visible = False
        self.fill_phone_content()
      else:
        self.phone_panel.visible = False
        self.pc_panel.visible = True
        self.fill_pc_content()
    # Any code you write here will run before the form opens.

  def edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..createAppointment import createAppointment
    popup = createAppointment(self.item)
    open_form(popup)

  def delete_button_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def fill_pc_content(self):
      self.lbl_name.text = "ID: " + self.item.get("name", "jeje")
      self.lbl_description.text = "Notas: " + self.item.get("notes", "miau")
      self.lbl_meds.text = "Medicamentos: " + self.item.get("meds", "miau")
      self.lbl_type.text = f"{self.item.get('type', 'miau')}: {self.item.get('money', 'miau')}€"
      self.lbl_date.text = f"{self.item.get('date', 'miau')}"
      timelapse = int(self.item.get('timelapse','0'))
      elapsed_minutes = timelapse // 60
      elapsed_seconds = timelapse % 60 
      self.lbl_timelapse.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"
    
  def fill_phone_content(self):
      self.lbl_name_copy.text = "ID: " + self.item.get("name", "jeje")
      self.lbl_description_copy.text = "Notas: " + self.item.get("notes", "miau")
      self.lbl_meds_copy.text = "Medicamentos: " + self.item.get("meds", "miau")
      self.lbl_type_copy.text = f"{self.item.get('type', 'miau')}: {self.item.get('money', 'miau')}€"
      self.lbl_date_copy.text = f"{self.item.get('date', 'miau')}"
      timelapse = int(self.item.get('timelapse','0'))
      elapsed_minutes = timelapse // 60
      elapsed_seconds = timelapse % 60 
      self.lbl_timelapse_copy.text = f"{elapsed_minutes:02}:{elapsed_seconds:02}"