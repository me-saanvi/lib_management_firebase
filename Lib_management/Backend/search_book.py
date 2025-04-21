from firebase_admin import firestore

def search_book(keyword):
    """
    Searches for books with titles containing the given keyword (case-insensitive).
    """
    try:
        db = firestore.client()
        books_ref = db.collection('books')
        books = books_ref.stream()

        keyword_lower = keyword.lower()
        found = False

        print(f"\n🔍 Search Results for '{keyword}':\n" + "-" * 40)
        for book in books:
            data = book.to_dict()
            title = data.get('title', '')
            if keyword_lower in title.lower():
                print(f"ID: {book.id}")
                print(f"Title: {title}")
                print(f"Author: {data.get('author', 'N/A')}")
                print(f"Published Year: {data.get('published_year', 'N/A')}")
                print(f"Genre: {data.get('genre', 'N/A')}")
                print("-" * 40)
                found = True

        if not found:
            print("No matching books found.")

    except Exception as e:
        print(f"Error searching books: {e}")
