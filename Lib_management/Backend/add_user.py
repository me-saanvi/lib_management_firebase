# Add a user to Firestore

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("config/firebase-credentials.json")  # Ensure the path is correct
    firebase_admin.initialize_app(cred)

db = firestore.client()

def add_user(user_id, username, email, borrowed_books=None):
    users_ref = db.collection('users')  # Reference to the 'users' collection

    # Set default value for borrowed_books if None
    if borrowed_books is None:
        borrowed_books = []

    # User data to be added
    user_data = {
        'user_id': user_id,
        'username': username,
        'email': email,
        'borrowed_books': borrowed_books,
    }

    # Add the user data
    users_ref.document(user_id).set(user_data)
    print(f"User added: {username} (ID: {user_id})")
