import logging
import pytest
import requests
import time

from datetime import datetime, timezone

from consts.network import Network
from validators.book_valiidator import BookValidator
from helpers.book_helpers import BookHelpers

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
        book_id = BookHelpers.generate_book_id()
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
        book_id = BookHelpers.generate_book_id()
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
        book_id = BookHelpers.generate_book_id()
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
        book_id = BookHelpers.generate_book_id()
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

    def test_create_book_with_invalid_id(self):
        self.log.info("test_create_book_with_invalid_id")
        payload = {
            "id": "book1",
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_duplicate_id(self):
        self.log.info("test_create_book_with_duplicate_id")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        # this one should fail - and not allow to post existing id
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_too_large_id(self):
        self.log.info("test_create_book_with_too_large_id")
        payload = {
            "id": 2147483648,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_empty_payload(self):
        self.log.info("test_create_book_with_too_large_id")
        payload = {}
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_missing_payload(self):
        self.log.info("test_create_book_with_too_large_id")
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}")
        assert self.validator.validate_unsupported_media_type_response(response)

    def test_create_book_with_invalid_page_count(self):
        self.log.info("test_create_book_with_invalid_page_count")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": "one hundred",
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_too_large_page_count(self):
        self.log.info("test_create_book_with_too_large_page_count")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 2147483648,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_invalid_publish_date(self):
        self.log.info("test_create_book_with_invalid_publishDate")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_missing_id(self):
        self.log.info("test_create_book_with_missing_id")
        payload = {
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_missing_title(self):
        self.log.info("test_create_book_with_missing_title")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_missing_description(self):
        self.log.info("test_create_book_with_missing_description")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "title": "Sed ut perspiciatis",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_missing_page_count(self):
        self.log.info("test_create_book_with_missing_page_count")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_missing_exerpt(self):
        self.log.info("test_create_book_with_missing_excerpt")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_create_book_with_missing_publish_date(self):
        self.log.info("test_create_book_with_missing_publish_date")
        payload = {
            "id": BookHelpers.generate_book_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    # backend may cast it into string - needs to be verified
    def test_create_book_with_invalid_title(self):
        self.log.info("test_create_book_with_invalid_title")
        book_id = BookHelpers.generate_book_id()
        payload = {
            "id": book_id,
            "title": 123456789,
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_ok_response(response)

    # backend may cast it into string - needs to be verified
    def test_create_book_with_invalid_description(self):
        self.log.info("test_create_book_with_invalid_description")
        book_id = BookHelpers.generate_book_id()
        payload = {
            "id": book_id,
            "title": "Sed ut perspiciatis",
            "description":123456789,
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_ok_response(response)

    # backend may cast it into string - needs to be verified
    def test_create_book_with_invalid_excerpt(self):
        self.log.info("test_create_book_with_invalid_excerpt")
        book_id = BookHelpers.generate_book_id()
        payload = {
            "id": book_id,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": 123456789,
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}", json=payload)
        assert self.validator.validate_ok_response(response)

    # this should not be allowed - primary key change
    def test_replace_book_invalid_id(self):
        self.log.info("test_replace_book_invalid_id")
        payload = {
            "id": "book1",
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    # this should not be allowed - primary key change
    def test_replace_book_too_large_id(self):
        self.log.info("test_replace_book_too_large_id")
        payload = {
            "id": 2147483648,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_empty_payload(self):
        self.log.info("test_replace_book_empty_payload")
        payload = {}
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_payload(self):
        self.log.info("test_replace_book_missing_payload")
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1")
        assert self.validator.validate_unsupported_media_type_response(response)

    def test_replace_book_invalid_page_count(self):
        self.log.info("test_replace_book_invalid_page_count")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": "one hundred",
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_too_large_page_count(self):
        self.log.info("test_replace_book_too_large_page_count")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 2147483648,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_invalid_publish_date(self):
        self.log.info("test_replace_book_invalid_publish_date")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 1234,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_id(self):
        self.log.info("test_replace_book_missing_id")
        payload = {
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 1234,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_title(self):
        self.log.info("test_replace_book_missing_title")
        payload = {
            "id": 1,
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 1234,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_description(self):
        self.log.info("test_replace_book_missing_description")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "pageCount": 1234,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_page_count(self):
        self.log.info("test_replace_book_missing_page_count")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_excerpt(self):
        self.log.info("test_replace_book_missing_excerpt")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 1234,
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_missing_publish_date(self):
        self.log.info("test_replace_book_missing_publish_date")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 1234,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_invalid_title(self):
        self.log.info("test_replace_book_invalid_title")
        payload = {
            "id": 1,
            "title": 123456789,
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 1234,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_invalid_description(self):
        self.log.info("test_replace_book_invalid_description")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":123456789,
            "pageCount": 1234,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)

    def test_replace_book_invalid_excerpt(self):
        self.log.info("test_replace_book_invalid_excerpt")
        payload = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 1234,
            "excerpt": 123456789,
            "publishDate": "today"
        }
        response = requests.put(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)
