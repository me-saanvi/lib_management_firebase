from firebase_admin import firestore

def delete_book(book_id):
    """
    Deletes a book document from the 'books' collection based on its document ID.
    """
    try:
        db = firestore.client()
        books_ref = db.collection('books')

        doc = books_ref.document(book_id).get()

        if doc.exists:
            books_ref.document(book_id).delete()
            print(f"Deleted book with ID: {book_id}")
        else:
            print(f"No book found with ID: {book_id}")

    except Exception as e:
        print(f"Error deleting book by ID: {e}")
