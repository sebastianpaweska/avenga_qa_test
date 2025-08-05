import logging
import pytest
import requests
import time

from consts.network import Network
from consts.payloads import AuthorsNullablePayload, AuthorsPostPayload, AuthorsPutPayload
from validators.author_validator import AuthorValidator
from helpers.book_helpers import BookHelpers

@pytest.mark.authors
class TestAuthors:
    @classmethod
    def setup_class(cls):
        cls.log = logging.getLogger("api_tests")
        cls.validator = AuthorValidator()

    @staticmethod
    def teardown():
        time.sleep(0.1)

    def test_get_authors(self):
        self.log.info("test_get_authors")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}")
        assert self.validator.validate_get_authors_response(response)

    # todo randomize id
    def test_get_single_author(self):
        self.log.info("test_get_authors")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/1")
        assert self.validator.validate_get_single_author_response(response)

    # todo randomize id
    def test_get_books_authors(self):
        self.log.info("test_get_books_authors")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS_BOOKS.value}/1")
        assert self.validator.validate_get_authors_response(response)
        # todo validate against something else?

    def test_delete_author(self):
        self.log.info("test_delete_author")
        response = requests.delete(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/1")
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/1")
        assert self.validator.validate_not_found_response(response)

    def test_create_author(self):
        self.log.info("test_create_author")
        author_id = BookHelpers.generate_id()
        book_id = BookHelpers.generate_id()
        payload = {
            "id": author_id,
            "idBook": book_id,
            "firstName": "Lorem",
            "lastName": "Ipsum",
        }
        response = requests.post(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/{author_id}")
        assert self.validator.validate_get_single_author_response(response)
        # todo create some validator here - make sure that book data matches the author id
        # but it will fail, so not implemented
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS_BOOKS.value}/1")
        assert self.validator.validate_get_authors_response(response)

    def test_replace_author(self):
        self.log.info("test_replace_author")
        author_id = 1
        book_id = BookHelpers.generate_id()
        payload = {
            "id": 1,
            "idBook": book_id,
            "firstName": "Ipslore",
            "lastName": "The Red",
        }
        response = requests.put(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/{author_id}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/{author_id}")
        assert self.validator.validate_get_single_author_response(response)
        # todo create some validator here - make sure that book data matches the author id
        # but it will fail, so not implemented
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS_BOOKS.value}/{author_id}")
        assert self.validator.validate_get_authors_response(response)

    @pytest.mark.parametrize(
        "payload_name,payload",
        [(p.name, p.value) for p in AuthorsNullablePayload],
        ids=[p.name.lower() for p in AuthorsNullablePayload]
    )
    def test_create_author_with_nullable(self, payload_name, payload):
        self.log.info("test_create_author_with_nullable: %s", payload_name)
        response = requests.post(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{payload["id"]}")
        assert self.validator.validate_get_single_author_response(response)

    @pytest.mark.parametrize(
        "payload_name,payload",
        [(p.name, p.value) for p in AuthorsNullablePayload],
        ids=[p.name.lower() for p in AuthorsNullablePayload]
    )
    def test_replace_author_with_nullable(self, payload_name, payload):
        self.log.info("test_replace_author_with_nullable: %s", payload_name)
        response = requests.put(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/{payload["id"]}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.BOOKS.value}/{payload["id"]}")
        assert self.validator.validate_get_single_author_response(response)

    # should create a new one
    def test_replace_nonexistent_author(self):
        self.log.info("test_replace_author")
        author_id = 999999
        book_id = BookHelpers.generate_id()
        payload = {
            "id": author_id,
            "idBook": book_id,
            "firstName": "Ipslore",
            "lastName": "The Red",
        }
        response = requests.put(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/{author_id}", json=payload)
        assert self.validator.validate_ok_response(response)
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/{author_id}")
        assert self.validator.validate_get_single_author_response(response)
        # todo create some validator here - make sure that book data matches the author id
        # but it will fail, so not implemented

    def test_get_nonexistent_author(self):
        self.log.info("test_get_nonexistent_author")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/123456789")
        assert self.validator.validate_not_found_response(response)

    def test_get_invalid_author(self):
        self.log.info("test_get_invalid_author")
        response = requests.get(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/author1")
        assert self.validator.validate_bad_request_response(response)

    def test_delete_nonexistent_author(self):
        self.log.info("test_delete_nonexistent_author")
        response = requests.delete(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/123456789")
        assert self.validator.validate_not_found_response(response)

    def test_delete_invalid_author(self):
        self.log.info("test_delete_invalid_author")
        response = requests.delete(f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/author1")
        assert self.validator.validate_bad_request_response(response)

    # skipping book/author tests due to the lack of time, not in scope

    def test_create_author_missing_payload(self):
        self.log.info("test_create_author_missing_payload")
        response = requests.post(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}")
        assert self.validator.validate_unsupported_media_type_response(response)

    def test_replace_author_missing_payload(self):
        self.log.info("test_replace_author_missing_payload")
        author_id = 1
        response = requests.put(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/{author_id}")
        assert self.validator.validate_unsupported_media_type_response(response)

    @pytest.mark.parametrize(
        "payload_name,payload",
        [(p.name, p.value) for p in AuthorsPostPayload],
        ids=[p.name.lower() for p in AuthorsPostPayload]
    )
    def test_create_author_negative(self, payload_name, payload):
        self.log.info("test_create_author_negative %s", payload_name)
        response = requests.post(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}", json=payload)
        assert self.validator.validate_bad_request_response(response)

    @pytest.mark.parametrize(
        "payload_name,payload",
        [(p.name, p.value) for p in AuthorsPutPayload],
        ids=[p.name.lower() for p in AuthorsPutPayload]
    )
    def test_replace_author_negative(self, payload_name, payload):
        self.log.info("test_replace_author_negative %s", payload_name)
        response = requests.put(
            f"{Network.PROTOCOL.value}://{Network.API_URL.value}{Network.AUTHORS.value}/1", json=payload)
        assert self.validator.validate_bad_request_response(response)
