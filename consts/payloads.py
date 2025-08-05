from enum import Enum
from helpers.book_helpers import BookHelpers


class BooksBasePayload:
    INVALID_ID = {
            "id": "book1",
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    # todo only difference?
    DUPLICATE_ID = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    TOO_LARGE_ID = {
            "id": 2147483648,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    EMPTY_PAYLOAD = {}
    INVALID_PAGE_COUNT = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": "one hundred",
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    TOO_LARGE_PAGE_COUNT = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 2147483648,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    INVALID_PUBLISH_DATE = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": "today"
        }
    MISSING_ID = {
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    MISSING_TITLE = {
            "id": BookHelpers.generate_id(),
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    MISSING_DESCRIPTION = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    MISSING_PAGE_COUNT = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    MISSING_EXCERPT = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    MISSING_PUBLISH_DATE = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
        }
    # backend may cast it into string - needs to be verified
    INVALID_TITLE = {
            "id": BookHelpers.generate_id(),
            "title": 123456789,
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    # backend may cast it into string - needs to be verified
    INVALID_DESCRIPTION = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":123456789,
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    # backend may cast it into string - needs to be verified
    INVALID_EXCERPT = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": 123456789,
            "publishDate": BookHelpers.generate_book_publish_date()
        }


class BooksPostPayloads(Enum):
    EMPTY_PAYLOAD = BooksBasePayload.EMPTY_PAYLOAD
    INVALID_ID = BooksBasePayload.INVALID_ID
    TOO_LARGE_ID = BooksBasePayload.TOO_LARGE_ID
    INVALID_PAGE_COUNT = BooksBasePayload.INVALID_PAGE_COUNT
    TOO_LARGE_PAGE_COUNT = BooksBasePayload.TOO_LARGE_PAGE_COUNT
    INVALID_PUBLISH_DATE = BooksBasePayload.INVALID_PUBLISH_DATE
    MISSING_ID = BooksBasePayload.MISSING_ID
    MISSING_TITLE = BooksBasePayload.MISSING_TITLE
    MISSING_DESCRIPTION = BooksBasePayload.MISSING_DESCRIPTION
    MISSING_PAGE_COUNT = BooksBasePayload.MISSING_PAGE_COUNT
    MISSING_EXCERPT = BooksBasePayload.MISSING_EXCERPT
    MISSING_PUBLISH_DATE = BooksBasePayload.MISSING_PUBLISH_DATE
    # backend may cast it into string - needs to be verified
    INVALID_TITLE = BooksBasePayload.INVALID_TITLE
    # backend may cast it into string - needs to be verified
    INVALID_DESCRIPTION = BooksBasePayload.INVALID_DESCRIPTION
    # backend may cast it into string - needs to be verified
    INVALID_EXCERPT = BooksBasePayload.INVALID_EXCERPT
    DUPLICATE_ID = {
            "id": 1,
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }


class BooksPutPayloads(Enum):
    EMPTY_PAYLOAD = BooksBasePayload.EMPTY_PAYLOAD
    # this should not be allowed - primary key change
    INVALID_ID = BooksBasePayload.INVALID_ID
    # this should not be allowed - primary key change
    TOO_LARGE_ID = BooksBasePayload.TOO_LARGE_ID
    INVALID_PAGE_COUNT = BooksBasePayload.INVALID_PAGE_COUNT
    TOO_LARGE_PAGE_COUNT = BooksBasePayload.TOO_LARGE_PAGE_COUNT
    INVALID_PUBLISH_DATE = BooksBasePayload.INVALID_PUBLISH_DATE
    MISSING_ID = BooksBasePayload.MISSING_ID
    MISSING_TITLE = BooksBasePayload.MISSING_TITLE
    MISSING_DESCRIPTION = BooksBasePayload.MISSING_DESCRIPTION
    MISSING_PAGE_COUNT = BooksBasePayload.MISSING_PAGE_COUNT
    MISSING_EXCERPT = BooksBasePayload.MISSING_EXCERPT
    MISSING_PUBLISH_DATE = BooksBasePayload.MISSING_PUBLISH_DATE
    # backend may cast it into string - needs to be verified
    INVALID_TITLE = BooksBasePayload.INVALID_TITLE
    # backend may cast it into string - needs to be verified
    INVALID_DESCRIPTION = BooksBasePayload.INVALID_DESCRIPTION
    # backend may cast it into string - needs to be verified
    INVALID_EXCERPT = BooksBasePayload.INVALID_EXCERPT


class BooksNullablePayloads(Enum):
    EMPTY_TITLE = {
        "id": BookHelpers.generate_id(),
        "title": "",
        "description": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
        "pageCount": 123,
        "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
        "publishDate": BookHelpers.generate_book_publish_date()
    }
    EMPTY_DESCRIPTION = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"",
            "pageCount": 123,
            "excerpt": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
    EMPTY_EXCERPT = {
            "id": BookHelpers.generate_id(),
            "title": "Sed ut perspiciatis",
            "description":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",
            "pageCount": 123,
            "excerpt": "",
            "publishDate": BookHelpers.generate_book_publish_date()
        }
