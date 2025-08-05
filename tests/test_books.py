import logging
import pytest
import requests
import time

from consts.network import Network
from validators.book_valiidator import BookValidator
from helpers.book_helpers import BookHelpers
from consts.payloads import BooksPostPayloads, BooksPutPayloads

@pytest.mark.books
class TestBooks:
    @classmethod
    def setup_class(cls):
        cls.log = logging.getLogger("api_tests")
        cls.validator = BookValidator()

    @staticmethod
    def teardown():
        time.sleep(0.1)

    def test_get_books(self):
        self.log.info("test_get_books")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}")
        assert self.validator.validate_get_books_response(response)

    # for better coverage - consider randomizing book id in a given range
    def test_get_single_book(self):
        self.log.info("test_get_single_book")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_get_single_book_response(response)

    @pytest.mark.xfail(reason="fake api")
    def test_create_book(self):
        self.log.info("test_create_book")
        book_id = BookHelpers.generate_id()
        payload = {
            "id": book_id,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{book_id}")
        assert self.validator.validate_get_single_book_response(response)

    @pytest.mark.xfail(reason="fake api")
    def test_replace_book(self):
        self.log.info("test_replace_book")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_get_single_book_response(response)
        # this will fail on that API
        assert self.validator.validate_book_replaced(response, payload)

    # is it needed to fill the db before running this test?
    @pytest.mark.xfail(reason="fake api")
    def test_delete_book(self):
        self.log.info("test_delete_book")
        response = requests.delete(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_ok_response(response)
        # make sure it was deleted - will fail
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_not_found_response(response)

    # nullable - creation should work, validation will fail
    @pytest.mark.xfail(reason="fake api")
    def test_create_book_with_empty_title(self):
        self.log.info("test_create_book_with_empty_title")
        book_id = BookHelpers.generate_id()
        payload = {
            "id": book_id,
            "title": "",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{book_id}")
        assert self.validator.validate_get_single_book_response(response)

    # nullable - creation should work, validation will fail
    @pytest.mark.xfail(reason="fake api")
    def test_create_book_with_empty_description(self):
        self.log.info("test_create_book_with_empty_description")
        book_id = BookHelpers.generate_id()
        payload = {
            "id": book_id,
            "title": "Sed ut perspiciatis",
            "description":"",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{book_id}")
        assert self.validator.validate_get_single_book_response(response)

    # nullable - creation should work, validation will fail
    @pytest.mark.xfail(reason="fake api")
    def test_create_book_with_empty_excerpt(self):
        self.log.info("test_create_book_with_empty_excerpt")
        book_id = BookHelpers.generate_id()
        payload = {
            "id": book_id,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{book_id}")
        assert self.validator.validate_get_single_book_response(response)

    @pytest.mark.xfail(reason="fake api")
    def test_replace_book_empty_title(self):
        self.log.info("test_replace_book_empty_title")
        payload = {
            "id": 1,
            "title": "",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_get_single_book_response(response)
        # this will fail on that API
        assert self.validator.validate_book_replaced(response, payload)

    @pytest.mark.xfail(reason="fake api")
    def test_replace_book_empty_description(self):
        self.log.info("test_replace_book_empty_description")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_get_single_book_response(response)
        # this will fail on that API
        assert self.validator.validate_book_replaced(response, payload)

    @pytest.mark.xfail(reason="fake api")
    def test_replace_book_empty_excerpt(self):
        self.log.info("test_replace_book")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_get_single_book_response(response)
        # this will fail on that API
        assert self.validator.validate_book_replaced(response, payload)

    # todo more cases to cover put tests, not enough time
    # changing ID  should not be allowed - primary key or sth
    # using nonexistent id should work and create a new one
    def test_replace_nonexistent_book(self):
        self.log.info("test_replace_nonexistent_book")
        book_id = 99999
        payload = {
            "id": book_id,
            "title": "Sed ut perspiciatis",
            "description": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{book_id}",
                                json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{book_id}")
        assert self.validator.validate_get_single_book_response(response)
        # this will fail on that API
        assert self.validator.validate_book_replaced(response, payload)

    # negative tests

    def test_get_nonexistent_single_book(self):
        self.log.info("test_get_nonexistent_single_book")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1234567890")
        assert self.validator.validate_not_found_response(response)

    def test_get_invalid_single_book(self):
        self.log.info("test_get_nonexistent_single_book")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/book1")
        assert self.validator.validate_bad_request_response(response)

    def test_delete_nonexistent_book(self):
        self.log.info("test_delete_nonexistent_book")
        response = requests.delete(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1234567")
        # this one should throw an error msg
        assert self.validator.validate_not_found_response(response)

    def test_delete_invalid_book(self):
        self.log.info("test_delete_invalid_book")
        response = requests.delete(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/book1")
        # this one should throw an error msg
        assert self.validator.validate_bad_request_response(response)

    @pytest.mark.parametrize(
        "payload_name,payload",
        [(p.name, p.value) for p in BooksPostPayloads],
        ids=[p.name.lower() for p in BooksPostPayloads]
    )
    def test_create_book_negative(self, payload_name, payload):
        self.log.info("test_create_book_negative: %s", payload_name)
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_missing_payload(self):
        self.log.info("test_create_book_with_too_large_id")
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}")
        assert self.validator.validate_unsupported_media_type_response(response)

    # this should not be allowed - primary key change
    @pytest.mark.parametrize(
        "payload_name,payload",
        [(p.name, p.value) for p in BooksPutPayloads],
        ids=[p.name.lower() for p in BooksPutPayloads]
    )
    def test_replace_book_negative(self, payload_name, payload):
        self.log.info("test_replace_book_negative")
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_payload(self):
        self.log.info("test_replace_book_missing_payload")
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_unsupported_media_type_response(response)
