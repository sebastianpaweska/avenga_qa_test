import logging

from validators.validator import Validator

logger = logging.getLogger("author_validator")

class AuthorValidator(Validator):

    @staticmethod
    def validate_author(author):
        try:
            assert "id" in author and isinstance(author["id"], int)
            logger.debug("validating author %s", author["id"])
            assert "idBook" in author and isinstance(author["idBook"], int)
            assert "firstName" in author and isinstance(author["firstName"], str)  # nullable
            assert "lastName" in author and isinstance(author["lastName"], str) # nullable
            return True
        except AssertionError as e:
            logger.error(repr(e))
            raise e

    def validate_get_authors_response(self, response):
        try:
            logger.debug("validating get books response")
            assert self.validate_ok_response(response)
            content = response.json()
            for author in content:
                assert self.validate_author(author)
            return True
        except AssertionError as e:
            logger.error(repr(e))
            raise e

    def validate_get_single_author_response(self, response):
        try:
            logger.debug("validating get single authr response")
            assert self.validate_ok_response(response)
            # todo validate content
            content = response.json()
            assert self.validate_author(content)
            return True
        except AssertionError as e:
            logger.error(repr(e))
            raise e
