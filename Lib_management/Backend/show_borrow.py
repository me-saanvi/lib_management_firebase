from firebase_admin import firestore

def show_borrow(user_id):
    db = firestore.client()
    users_ref = db.collection('users')  # Reference to the 'users' collection
    
    # Query to get user by user_id field
    query = users_ref.where('user_id', '==', user_id).limit(1)
    user_doc = query.stream()

    # If the user exists
    found_user = False
    for user in user_doc:
        user_data = user.to_dict()
        borrowed_books = user_data.get('borrowed_books', [])
        print(f"User {user_id} has borrowed the following books: {borrowed_books}")
        found_user = True
        break  # Since we only expect one user with that user_id
    
    if not found_user:
        print(f"User with ID {user_id} does not exist.")
