import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("config/firebase-credentials.json")  # Ensure the path is correct
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Function to add a book (this will be your existing add_book function)
def add_book(book_id, title, author, published_year, genre):
    try:
        
        books_ref = db.collection('books')

        book_data = {
            'id': book_id,
            'title': title,
            'author': author,
            'published_year': published_year,
            'genre': genre,
            
        }

        books_ref.document(book_id).set(book_data)  # Assigns book_id as the document ID
        print(f"Book '{title}' added with ID: {book_id}")
        print(f"Book Details: ID: {book_id}, Title: {title}, Author: {author}, Published Year: {published_year}, Genre: {genre}")

    except Exception as e:
        print(f"An error occurred while adding the book: {e}")