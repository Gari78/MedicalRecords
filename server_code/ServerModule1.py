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
      return res
    
    except anvil.http.HttpError as e:
      print("Status code:", e.status)
      print("Cuerpo del error:", e)
      return({"status":e.status, "content":str(e)})
      #return {"content": [{"name": "Normal", "money": 7.4}, {"name": "Telemático", "money":7},{"name": "Urgente", "money":10},{"name": "Privado", "money":25}], "status": 200}
  
@anvil.server.callable
def get_all_appointments(initDate = None, endDate = None, type_id = None):
    try:
      urlCall="http://46.24.211.201:5000/api/v1/appointments/?doctor=76bf31f8-538a-4d99-8d45-26f5d39528fb"
      if initDate and endDate:
        urlCall = f"{urlCall}&initDate={initDate}&endDate={endDate}"
      if type_id:
        urlCall = f"{urlCall}&type={type_id}"
      res = anvil.http.request(
          url=urlCall,
          method="GET",
          json=True
      )
      res = {"status": 200, "content": res}
      return res
    
    except anvil.http.HttpError as e:
      print("Status code:", e.status)
      print("Cuerpo del error:", e)
      return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def create_appointment(appt):
  appt["doctor"] = "76bf31f8-538a-4d99-8d45-26f5d39528fb"
  try:
    res = anvil.http.request(
        url="http://46.24.211.201:5000/api/v1/appointments/",
        method="POST",
        data=appt,
        json=True
    )
    res = {"status": 201, "content": res}
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def update_appointment(appt,id):
  appt["doctor"] = "76bf31f8-538a-4d99-8d45-26f5d39528fb"
  try:
    res = anvil.http.request(
        url=f"http://46.24.211.201:5000/api/v1/appointments/{id}/",
        method="PATCH",
        data=appt,
        json=True
    )
    res = {"status": 200, "content": res}
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
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})

@anvil.server.callable
def get_all_reports(initDate = None, endDate = None):
    try:
      urlCall="http://46.24.211.201:5000/api/v1/reports/?doctor=76bf31f8-538a-4d99-8d45-26f5d39528fb"
      if initDate and endDate:
        urlCall = f"{urlCall}&initDate={initDate}&endDate={endDate}"
      res = anvil.http.request(
          url=urlCall,
          method="GET",
          json=True
      )
      res = {"status": 200, "content": res}
      return res
    
    except anvil.http.HttpError as e:
      print("Status code:", e.status)
      print("Cuerpo del error:", e)
      return({"status":e.status, "content":str(e)})

@anvil.server.callable
def create_report(appt):
  appt["doctor"] = "76bf31f8-538a-4d99-8d45-26f5d39528fb"
  try:
    res = anvil.http.request(
        url="http://46.24.211.201:5000/api/v1/reports/",
        method="POST",
        data=appt,
        json=True
    )
    res = {"status": 201, "content": res}
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def update_report(appt,id):
  appt["doctor"] = "76bf31f8-538a-4d99-8d45-26f5d39528fb"
  try:
    res = anvil.http.request(
        url=f"http://46.24.211.201:5000/api/v1/reports/{id}/",
        method="PATCH",
        data=appt,
        json=True
    )
    res = {"status": 200, "content": res}
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})