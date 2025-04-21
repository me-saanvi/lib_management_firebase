from firebase_admin import firestore

def delete_user(user_id):
    """
    Deletes a user document from the 'users' collection based on the provided user_id.
    """
    try:
        db = firestore.client()
        users_ref = db.collection('users')
        
        # Attempt to delete the document with the specified user_id
        doc = users_ref.document(user_id).get()
        if doc.exists:
            users_ref.document(user_id).delete()
            print(f"✅ Deleted user with ID: {user_id}")
        else:
            print(f"⚠️ No user found with ID: {user_id}")
    
    except Exception as e:
        print(f"Error deleting user: {e}")
