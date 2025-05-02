from ._anvil_designer import TemplateTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
from anvil import js
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Template(TemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def appointmentsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Appointments')

  def statisticsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('stats')

  def reportsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def reset_links(self, **event_args):
    self.statisticsLink.role = ''
    self.appointmentsLink.role = ''
    self.reportsLink.role = ''

  def dutyLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Duty')

  def get_browser_timezone_offset(self):
    """Obtiene el offset de la zona horaria del navegador del usuario en minutos"""
    # Esto accede a la API JavaScript del navegador para obtener la zona horaria local
    return anvil.js.window.new(anvil.js.Date()).getTimezoneOffset()
  
  def get_browser_timezone_name(self):
    """Intenta obtener el nombre de la zona horaria del navegador"""
    try:
      # Esto funciona en navegadores modernos pero puede no ser compatible con todos
      return anvil.js.Intl.DateTimeFormat().resolvedOptions().timeZone
    except:
        return None
  
  def format_date_with_timezone(self,dt):
    """Formatea una fecha Python con la zona horaria del navegador"""
    if not isinstance(dt, datetime):
      return None
  
      # Obtener el offset en minutos (negativo porque getTimezoneOffset devuelve el contrario)
      offset_minutes = -self.get_browser_timezone_offset()
  
    # Calcular horas y minutos
    hours = int(offset_minutes / 60)
    minutes = abs(offset_minutes % 60)
  
    # Construir el string de offset
    sign = '+' if hours >= 0 else '-'
    offset_str = f"{sign}{abs(hours):02d}:{minutes:02d}"
  
    # Formatear la fecha
    return dt.isoformat().replace(" ", "T") + offset_str

