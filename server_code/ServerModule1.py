import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_all_types():
  return {"content": [{"name": "Normal", "money": 7.4}, {"name": "Telemático", "money":7},{"name": "Urgente", "money":10},{"name": "Privado", "money":25}], "status": 200}
  
@anvil.server.callable
def get_all_appointments():
    print("oleoleole!!!")
    return {
        "content":[
        {"name": "235769dkj", "notes": "Le dolía el alma", "type": "Normal", "money": "7,4", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "jdj532gds", "notes": "El bombero con dolor de abdominales", "type": "Urgente", "money": "10", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "jf84jdo20", "notes": "Zanahorio", "type": "Privado", "money": "25", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "8fdg73hds", "notes": "Gato filósofo", "type": "Normal", "money": "7,4", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "4jfk93kdl", "notes": "Un pez llamado Juan", "type": "Privado", "money": "25", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "0djh392fk", "notes": "La montaña de los sueños", "type": "Urgente", "money": "10", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "9gdh28sjk", "notes": "Mago sin varita", "type": "Normal", "money": "7,4", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "kl39dkf02", "notes": "Camino de caramelos", "type": "Privado", "money": "25", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "p2jfk38d9", "notes": "El hombre que hablaba con sombras", "type": "Urgente", "money": "10", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "z8fk392ld", "notes": "Biblioteca encantada", "type": "Normal", "money": "7,4", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "xj29fk30s", "notes": "Dragón dormilón", "type": "Privado", "money": "25", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "m3ldk49jf", "notes": "Pirata sin barco", "type": "Urgente", "money": "10", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "h4dk39sla", "notes": "Los zapatos del destino", "type": "Normal", "money": "7,4", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"}
      ], "status": 201
    }

def create_appointment(data):
  return {"id": 1, "status":200}

def edit_appointment(data):
  return {"id": 1, "status":200}
#
def get_all_reports():
  return {
    "content":[
        {"name": "235769dkj", "notes": "Le dolía el alma", "init_date": "20/02/2025", 
         "end_date": "19/03/2025", "income": {"gross": 2125, "net": 1875},
         "patiens":{
           "total": {"quantity":251, "money":7.4}, 
           "normal": {"quantity":251, "money":7.4},"telematic": {"quantity":251, "money":7.4},
           "urgent": {"quantity":251, "money":7.4},"patients": {"quantity":251, "money":7.4}
         }, 
        },
        {"name": "jdj532gds", "notes": "El bombero con dolor de abdominales", "type": "Urgente", "money": "10", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "jf84jdo20", "notes": "Zanahorio", "type": "Privado", "money": "25", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"},
        {"name": "8fdg73hds", "notes": "Gato filósofo", "type": "Normal", "money": "7,4", "date":"01-01-2025", "timelapse": "420", "meds": "Therearenomeds"}
    ], "status":200
  }