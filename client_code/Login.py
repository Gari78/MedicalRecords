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


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    res = self.login_keycloak(email = self.mail_input.text, pwd = self.pwd_input.text)
    if res["status"] == 200:
      open_form('Home')
    else:
      alert("El usuario o contraseña introducidos no son correctos", title="Error Autenticación", large=True, buttons=[("OK", None)])

  def mail_input_focus(self, **event_args):
    self.mail_input.text = "" if "Correo Elec" in self.mail_input.text else self.mail_input.text
    
  def pwd_input_focus(self, **event_args):
    self.pwd_input.text = "" if "Contraseña" in self.pwd_input.text else self.pwd_input.text

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def login_keycloak(self, email, pwd):
    if email == "alfonso.garijo@soologic.com" and pwd == "aerosmith":
      return {"status": 200}
    else:
      return {"status": 401}