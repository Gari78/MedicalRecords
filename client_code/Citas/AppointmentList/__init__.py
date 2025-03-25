from ._anvil_designer import AppointmentListTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AppointmentList(AppointmentListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.item:
      self.lbl_name.text = self.item.get("nombre", "jeje")
      self.lbl_description.text = self.item.get("descripcion", "miau")
      self.lbl_type.text = self.item.get("tipo", "miau")
      self.lbl_money.text = f"{self.item.get('dinero', 'miau')} €"

    # Any code you write here will run before the form opens.
