from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def mail_input_focus(self, **event_args):
    self.mail_input.text = "" if "Correo Elec" in self.mail_input.text else self.mail_input.text
    
  def pwd_input_focus(self, **event_args):
    self.pwd_input.text = "" if "Contraseña" in self.pwd_input.text else self.pwd_input.text

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def
