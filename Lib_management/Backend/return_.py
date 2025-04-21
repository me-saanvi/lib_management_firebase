from firebase_admin import firestore
from datetime import datetime

db = firestore.client()

def return_book(user_id, book_id):
    try:
        users_ref = db.collection('users').document(user_id)
        user_doc = users_ref.get()

        if not user_doc.exists:
            return f"User with ID {user_id} does not exist."

        user_data = user_doc.to_dict()
        borrowed_books = user_data.get('borrowed_books', [])

        if book_id not in borrowed_books:
            return f"Book with ID {book_id} is not borrowed by user {user_id}."

        # Remove the book from user's borrowed list
        borrowed_books.remove(book_id)
        users_ref.update({'borrowed_books': borrowed_books})

        # Optionally, delete from borrowed_books collection
        borrowed_collection = db.collection('borrowed_books')
        borrowed_query = borrowed_collection.where('user_id', '==', user_id).where('book_id', '==', book_id).stream()
        for record in borrowed_query:
            borrowed_collection.document(record.id).delete()

        return f"Book {book_id} returned successfully by user {user_id}."

    except Exception as e:
        return f"Error returning book: {e}"
