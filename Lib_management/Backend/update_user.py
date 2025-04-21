from firebase_admin import firestore

def update_user(user_id, updated_data):
    """
    Updates user information for a given user_id in the 'users' collection.

    Parameters:
    - user_id (str): The ID of the user document to update.
    - updated_data (dict): A dictionary of fields to update, e.g., {'name': 'New Name'}
    """
    try:
        db = firestore.client()
        users_ref = db.collection('users')
        user_doc = users_ref.document(user_id).get()

        if user_doc.exists:
            users_ref.document(user_id).update(updated_data)
            print(f"✅ User with ID {user_id} updated successfully.")
        else:
            print(f"⚠️ No user found with ID {user_id}.")

    except Exception as e:
        print(f"Error updating user: {e}")
