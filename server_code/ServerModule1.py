import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def login(email,password):
  try:
    body_auth = {"email": email, "password": password}
    res = anvil.http.request(
        url="http://46.24.211.201:5000/api/v1/login/",
        method="POST",
        data=body_auth,
        json=True
    )
    res["status"] = 200
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def get_all_appointment_types():
    try:
      res = anvil.http.request(
          url="http://46.24.211.201:5000/api/v1/appointment_types/?fields=id,name,value",
          method="GET",
          json=True
      )
      res = {"status": 200, "content": res}
      print(res)
      return res
    
    except anvil.http.HttpError as e:
      print("Status code:", e.status)
      print("Cuerpo del error:", e)
      return({"status":e.status, "content":str(e)})
      #return {"content": [{"name": "Normal", "money": 7.4}, {"name": "Telemático", "money":7},{"name": "Urgente", "money":10},{"name": "Privado", "money":25}], "status": 200}
  
@anvil.server.callable
def get_all_appointments():
    try:
      res = anvil.http.request(
          url="http://46.24.211.201:5000/api/v1/appointments/",
          method="GET",
          json=True
      )
      res = {"status": 200, "content": res}
      print(res)
      return res
    
    except anvil.http.HttpError as e:
      print("Status code:", e.status)
      print("Cuerpo del error:", e)
      return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def create_appointment(appt):
  print(appt)
  try:
    res = anvil.http.request(
        url="http://46.24.211.201:5000/api/v1/appointments/",
        method="POST",
        data=appt,
        json=True
    )
    res = {"status": 201, "content": res}
    print(res)
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def update_appointment(appt,id):
  print(appt)
  try:
    res = anvil.http.request(
        url=f"http://46.24.211.201:5000/api/v1/appointments/{id}/",
        method="PATCH",
        data=appt,
        json=True
    )
    res = {"status": 200, "content": res}
    print(res)
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def delete_appointment(id):
  try:
    res = anvil.http.request(
        url=f"http://46.24.211.201:5000/api/v1/appointments/{id}/",
        method="DELETE",
        json=True
    )
    res = {"status": 200, "content": res}
    print(res)
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})

@anvil.server.callable
def get_all_reports():
  return {
    "content":[
      {
        "name": "Febrero",
        "notes": "vaya hartura de trabajar",
        "init_date": "20/02/2025",
        "end_date": "19/03/2025",
        "income": {"gross": 2194, "net": 1755.2},
        "patients": {
          "total": {"quantity": 251, "money": 2194},
          "normal": {"quantity": 110, "money": 814},
          "telematic": {"quantity": 90, "money": 630},
          "urgent": {"quantity": 35, "money": 350},
          "private": {"quantity": 16, "money": 400}
        }
      },
      {
        "name": "Marzo",
        "notes": "mes tranquilo pero constante",
        "init_date": "20/03/2025",
        "end_date": "19/04/2025",
        "income": {"gross": 2328, "net": 1862.4},
        "patients": {
          "total": {"quantity": 270, "money": 2328},
          "normal": {"quantity": 120, "money": 888},
          "telematic": {"quantity": 95, "money": 665},
          "urgent": {"quantity": 40, "money": 400},
          "private": {"quantity": 15, "money": 375}
        }
      },
      {
        "name": "Abril",
        "notes": "menos pacientes por Semana Santa",
        "init_date": "20/04/2025",
        "end_date": "19/05/2025",
        "income": {"gross": 2170, "net": 1736.0},
        "patients": {
          "total": {"quantity": 240, "money": 2170},
          "normal": {"quantity": 100, "money": 740},
          "telematic": {"quantity": 90, "money": 630},
          "urgent": {"quantity": 30, "money": 300},
          "private": {"quantity": 20, "money": 500}
        }
      },
      {
        "name": "Mayo",
        "notes": "repunte de actividad",
        "init_date": "20/05/2025",
        "end_date": "19/06/2025",
        "income": {"gross": 2775, "net": 2220},
        "patients": {
          "total": {"quantity": 295, "money": 2775},
          "normal": {"quantity": 125, "money": 925},
          "telematic": {"quantity": 100, "money": 700},
          "urgent": {"quantity": 40, "money": 400},
          "private": {"quantity": 30, "money": 750}
        }
      },
      {
        "name": "Junio",
        "notes": "calorcito y muchas consultas privadas",
        "init_date": "20/06/2025",
        "end_date": "19/07/2025",
        "income": {"gross": 3491, "net": 2792.8},
        "patients": {
          "total": {"quantity": 310, "money": 3491},
          "normal": {"quantity": 115, "money": 851},
          "telematic": {"quantity": 95, "money": 665},
          "urgent": {"quantity": 35, "money": 350},
          "private": {"quantity": 65, "money": 1625}
        }
      }
    ], "status":200
  }