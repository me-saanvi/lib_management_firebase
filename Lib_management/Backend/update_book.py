from firebase_admin import firestore

def update_book(book_id, updated_data):
    """
    Updates fields of a book document in the 'books' collection by its document ID.
    
    :param book_id: Firestore document ID of the book
    :param updated_data: Dictionary of fields to update, e.g., {'title': 'New Title'}
    """
    try:
        db = firestore.client()
        book_ref = db.collection('books').document(book_id)
        
        # Check if book exists
        if not book_ref.get().exists:
            print(f"No book found with ID: {book_id}")
            return

        book_ref.update(updated_data)
        print(f"✅ Book with ID '{book_id}' updated successfully!")

    except Exception as e:
        print(f"Error updating book: {e}")
