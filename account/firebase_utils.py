# login_app/firebase_utils.py
from firebase_admin import firestore

# Initialize Firestore
db = firestore.client()

def get_user_data(email):
    doc_ref = db.collection('users').document(email)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def set_user_data(email, data):
    doc_ref = db.collection('users').document(email)
    doc_ref.set(data)
