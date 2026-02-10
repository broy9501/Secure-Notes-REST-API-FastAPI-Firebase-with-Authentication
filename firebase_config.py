# Intialize firebase admin sdk and database reference

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(
    "crendentials.json"
)

firebase_admin.initialize_app(cred, {"databaseURL": "database.app/"})

database = db.reference()

