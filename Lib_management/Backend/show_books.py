from firebase_admin import firestore

def show_books():
    """
    Fetches and prints all books in the 'books' collection.
    """
    try:
        db = firestore.client()
        books_ref = db.collection('books')
        books = books_ref.stream()

        found = False
        print("\n📚 Books in the Library:\n" + "-" * 40)
        for book in books:
            data = book.to_dict()
            print(f"ID: {book.id}")
            print(f"Title: {data.get('title', 'N/A')}")
            print(f"Author: {data.get('author', 'N/A')}")
            print(f"Published Year: {data.get('published_year', 'N/A')}")
            print(f"Genre: {data.get('genre', 'N/A')}")
            print("-" * 40)
            found = True

        if not found:
            print("No books found in the database.")

    except Exception as e:
        print(f"Error fetching books: {e}")
