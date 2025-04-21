from firebase_admin import firestore

def borrow_book(user_id, book_id, borrow_duration):
    db = firestore.client()
    users_ref = db.collection('users')
    books_ref = db.collection('books')
    
    # Get user document by user_id
    user_doc = users_ref.where('user_id', '==', user_id).limit(1).stream()
    user_found = False
    for user in user_doc:
        user_data = user.to_dict()
        borrowed_books = user_data.get('borrowed_books', [])
        
        # Check if the book is already borrowed
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)  # Add the book ID to the borrowed books list
            users_ref.document(user.id).update({'borrowed_books': borrowed_books})  # Update the user document
            print(f"User {user_id} borrowed the book with ID {book_id}.")
            user_found = True
            break
        
    if not user_found:
        print(f"User with ID {user_id} does not exist.")
