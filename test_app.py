import unittest
from pathlib import Path

HTML = Path("index.html").read_text(encoding="utf-8")

class BookstoreTests(unittest.TestCase):

    def test_six_books_exist(self):
        self.assertGreaterEqual(HTML.count('class="book"'), 6)

    def test_search_feature_exists(self):
        self.assertIn("function searchBooks()", HTML)

    def test_cart_feature_exists(self):
        self.assertIn("function addToCart", HTML)

    def test_checkout_feature_exists(self):
        self.assertIn("function checkout()", HTML)

    def test_thank_you_message_exists(self):
        self.assertIn("Thank you!", HTML)

    def test_availability_labels_exist(self):
        self.assertIn("In Stock", HTML)
        self.assertIn("Out of Stock", HTML)


if __name__ == "__main__":
    unittest.main()
