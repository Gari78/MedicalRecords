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
def secure_endpoint_call(url, data: dict=None, method: str="GET", json: bool=True):
  #print(data)
  #print(url)
  #print(method)
  auth_token = anvil.server.session.get('auth_token', None)
  if not auth_token:
    return {"res": "not authenticated", "status": 401}
  headers = {'Authorization': f"Bearer {auth_token}"}

  if data is not None:
    res = anvil.http.request(
          url=url,
          method=method,
          data=data,
          json=True
      )
  else:
    res = anvil.http.request(
          url=url,
          method=method,
          json=True
      )
    
  return res

@anvil.server.callable
def login(email,password):
  try:
    body_auth = {"email": email, "password": password}
    #print(body_auth)
    res = anvil.http.request(
        url="http://46.25.119.157:5000/api/v1/login/",
        method="POST",
        data=body_auth,
        json=True
    )
    #print(res)
    anvil.server.session['auth_token'] = res["access_token"]
    anvil.server.session['user_info'] = res["user_info"]
    res["status"] = 200
    return res
  
  except anvil.http.HttpError as e:
    print("Status code:", e.status)
    print("Cuerpo del error:", e)
    return({"status":e.status, "content":str(e)})
  
@anvil.server.callable
def get_all_appointment_types():
    try:
      res = secure_endpoint_call(
          url="http://46.25.119.157:5000/api/v1/appointment_types/?fields=id,name,value",
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
    print(anvil.server.session.get('user_info', None))
    try:
      urlCall=f"http://46.25.119.157:5000/api/v1/appointments/?doctor={anvil.server.session['user_info']['id']}"
      if initDate and endDate:
        urlCall = f"{urlCall}&initDate={initDate}&endDate={endDate}"
      if type_id:
        urlCall = f"{urlCall}&type={type_id}"
      res = secure_endpoint_call(
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
  appt["doctor"]  = anvil.server.session['user_info']['id']
  try:
    res = secure_endpoint_call(
        url="http://46.25.119.157:5000/api/v1/appointments/",
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
  appt["doctor"]  = anvil.server.session['user_info']['id']
  try:
    res = secure_endpoint_call(
        url=f"http://46.25.119.157:5000/api/v1/appointments/{id}/",
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
    res = secure_endpoint_call(
        url=f"http://46.25.119.157:5000/api/v1/appointments/{id}/",
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
      urlCall=f"http://46.25.119.157:5000/api/v1/reports/?doctor={anvil.server.session['user_info']['id']}"
      if initDate and endDate:
        urlCall = f"{urlCall}&initDate={initDate}&endDate={endDate}"
      res = secure_endpoint_call(
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