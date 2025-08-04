import logging

from http import HTTPStatus

logger = logging.getLogger("validator")

class Validator:
    @staticmethod
    def validate_ok_response(response):
        try:
            logger.debug("got response: %s", response.status_code)
            assert response.status_code == HTTPStatus.OK
            return True
        except AssertionError as e:
            raise e

    @staticmethod
    def validate_not_found_response(response):
        try:
            logger.debug("got response: %s", response.status_code)
            assert response.status_code == HTTPStatus.NOT_FOUND
            return True
        except AssertionError as e:
            raise e

    @staticmethod
    def validate_bad_request_response(response):
        try:
            logger.debug("got response: %s", response.status_code)
            assert response.status_code == HTTPStatus.BAD_REQUEST
            return True
        except AssertionError as e:
            raise e

    @staticmethod
    def validate_unsupported_media_type_response(response):
        try:
            logger.debug("got response: %s", response.status_code)
            assert response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE
            return True
        except AssertionError as e:
            raise e