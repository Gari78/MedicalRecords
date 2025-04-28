from ._anvil_designer import createReportTemplate
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
from datetime import datetime, timezone


class createReport(createReportTemplate):
  def __init__(self, report=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.report = report  # Guardamos la report por si es una edición
    print(f"Report: {report}")

    if self.report:
      # Rellenar los campos con los datos existentes
      self.name_input.text = str(report.get("name", ""))
      self.description_input.text = report.get("comment", "")
      self.init_date_picker.date = datetime.fromisoformat(report.get("initdate", "").replace("Z", "+00:00"))      
      self.end_date_picker.date = datetime.fromisoformat(report.get("enddate", "").replace("Z", "+00:00")) 

  def save_button_click(self, **event_args):
    if self.report:
      appt = {
        "name": self.name_input.text,
        "comment": self.description_input.text,
        "initDate": self.init_date_picker.date.isoformat(),
        "endDate": self.end_date_picker.date.isoformat()
      }
      updated = anvil.server.call("update_appointment", appt, self.cita.get("id", 0))
    else:
      appt = {
        "name": self.name_input.text,
        "comment": self.description_input.text,
        "initDate": self.init_date_picker.date.isoformat(),
        "endDate": self.end_date_picker.date.isoformat()
      }
      created = anvil.server.call("create_appointment", appt)
    open_form("reports")

  def discard_button_click(self, **event_args):
    open_form("reports")

  def getRequest(self):
    token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4SU9OdS1tQnlpN2N3TmpoNUlTOXdzLXdyRm83NXBVMEhfRWQyOVladkQ4In0.eyJleHAiOjE3NDI3ODk4NDQsImlhdCI6MTc0Mjc1Mzg0NCwianRpIjoiM2YwNDAyMjItNTc1Yi00NmQ3LWFhOTAtY2EyMmU1NTQyZWE2IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9NZWRpY2FsUmVjb3JkcyIsImF1ZCI6InJlYWxtLW1hbmFnZW1lbnQiLCJzdWIiOiI3MDFmMjk2NS1hMTRjLTRkMjItYTJlYS1jYzI3ODVmOGQ3MDMiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJhcHAiLCJzaWQiOiIzM2I1NTA3YS1mNjFlLTQ2ZTItYWIzMS00ZjdmZWRkYWM5MzEiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJhZG1pbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1pZGVudGl0eS1wcm92aWRlcnMiLCJ2aWV3LXJlYWxtIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6ImFkbWluX3VzZXJzIiwiZW1haWwiOiJhZG1pbl91c2VyczEua2V5Y2xvYWtAc29vbG9naWMuY29tIn0.lpFMIiJ4-T5UqveKvh_hddW51lBuEofhzgEEJOX0nIcH4Gt1f2jwuV01z6XBwC1qB3cSDrYa0kLQyHIxJCeumEFvFhN7bZKMbDg0lFqinC5xU5arm77_ceJttL0NGybo3iNVFEsIxEvwdT3uJQC0QZWJKG2GwtDLnkU2x0EOgTQ8ARGCJHnFM7uEmwmsc3ANXdyQP_CoMNGRMEyTu8ojv2Rgr0MmCO7Q7QDZcFNggtbDtvKLjsim8CK2js-B7DOAf7528WDVMv8p6EbEWWNRapGck4NKIEkneGlJIgaBHynrDwnZS-i8S2mlJUQdI1DOIK8AGiThwf70h5AkHLwgww"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    # response = anvil.http.request("http://94.248.72.87:5000/api/v1/appointment_types/", method="GET", headers=headers, json=True)
    # return response

  def name_input_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.name_input.text = "" if "Nombre del informe" in self.name_input.text else self.name_input.text

  def description_input_focus(self, **event_args):
    """This method is called when the text area gets focus"""
    self.description_input.text = (
      "" if "Notas" == self.description_input.text else self.description_input.text
    )
