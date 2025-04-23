from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert
from anvil.js import window


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if window.innerHeight > window.innerWidth:
      self.xy_panel.height = window.innerHeight
      self.xy_panel_column.height = window.innerHeight
      self.xy_panel_column.width = window.innerWidth * 0.9
      self.spacer_1.height = window.innerHeight * 0.25
    else:
      self.xy_panel.height = window.innerHeight * 0.85
      self.xy_panel_column.height = window.innerHeight * 0.85

  def login_button_click(self, **event_args):
    res = anvil.server.call("login",self.mail_input.text,self.pwd_input.text)
    if res["status"] == 200:
      open_form('Appointments')
    else:
      alert(f"error {res['content']}", title="Error Autenticación", large=True, buttons=[("OK", None)])

  def mail_input_focus(self, **event_args):
    self.mail_input.text = "" if "Correo Elec" in self.mail_input.text else self.mail_input.text
    
  def pwd_input_focus(self, **event_args):
    self.pwd_input.text = "" if "Contraseña" in self.pwd_input.text else self.pwd_input.text

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Appointments')