from firebase_admin import firestore

def show_users():
    """
    Displays all users from the 'users' collection in Firestore.
    """
    try:
        db = firestore.client()
        users_ref = db.collection('users')
        users = users_ref.stream()

        found = False
        for user in users:
            print(f"User ID: {user.id} | Data: {user.to_dict()}")
            found = True

        if not found:
            print("No users found.")

    except Exception as e:
        print(f"Error displaying users: {e}")
