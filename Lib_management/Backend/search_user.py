from firebase_admin import firestore

def search_user(field_name, value):
    """
    Searches for users in the 'users' collection where field_name == value.

    Parameters:
    - field_name (str): The field to search by (e.g., 'name', 'email')
    - value (str): The value to search for

    Example:
        search_user_by_field('name', 'John Doe')
    """
    try:
        db = firestore.client()
        users_ref = db.collection('users')
        query = users_ref.where(field_name, '==', value)
        results = query.stream()

        found = False
        for user in results:
            print(f"✅ User Found: ID = {user.id}, Data = {user.to_dict()}")
            found = True

        if not found:
            print(f"❌ No user found where {field_name} == '{value}'")

    except Exception as e:
        print(f"Error searching for user: {e}")
