import logging

from datetime import datetime

from validators.validator import Validator

logger = logging.getLogger("book_validator")

class BookValidator(Validator):

    @staticmethod
    def validate_book(book):
        try:
            assert "id" in book and isinstance(book["id"], int)
            logger.debug("validating book %s", book["id"])
            assert "title" in book and isinstance(book["title"], str)  # nullable
            assert "description" in book and isinstance(book["description"], str)  # nullable
            assert "pageCount" in book and isinstance(book["pageCount"], int)
            assert "excerpt" in book and isinstance(book["excerpt"], str)  # nullable
            assert "publishDate" in book
            try:
                datetime.fromisoformat(book["publishDate"].replace("Z", "+00:00"))
                return True
            except ValueError:
                assert False, f"Invalid ISO datetime format: {book['publishDate']}"
        except AssertionError as e:
            logger.error(repr(e))
            raise e

    def validate_get_books_response(self, response):
        try:
            logger.debug("validating get books response")
            assert self.validate_ok_response(response)
            # todo validate content
            content = response.json()
            for book in content:
                assert self.validate_book(book)
            return True
        except AssertionError as e:
            logger.error(repr(e))
            raise e

    def validate_get_single_book_response(self, response):
        try:
            logger.debug("validating get books response")
            assert self.validate_ok_response(response)
            # todo validate content
            content = response.json()
            assert self.validate_book(content)
            return True
        except AssertionError as e:
            logger.error(repr(e))
            raise e

    @staticmethod
    def validate_book_replaced(response, expected_data):
        try:
            logger.debug("validating replaced book response")
            content = response.json()
            content_keys = set(content.keys())
            expected_keys = set(expected_data.keys())
            shared_keys = content_keys.intersection(expected_keys)
            modified = {o: (content[o], expected_data[o]) for o in shared_keys if content[o] != expected_data[o]}
            assert not modified
            return True
        except AssertionError as e:
            logger.error(repr(e))
            raise e
