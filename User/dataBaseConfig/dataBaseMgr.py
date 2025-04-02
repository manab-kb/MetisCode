import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.

current_dir = os.path.dirname(os.path.abspath(__file__))
cert_path = os.path.join(current_dir, 'datakey.json')
cred = credentials.Certificate(cert_path)

app = firebase_admin.initialize_app(cred)

db = firestore.client()

