import random
from datetime import datetime, timezone

class BookHelpers:
    @staticmethod
    def generate_id():
        max_int32 = 2 ** 31 - 1
        # for the purpose of testing this API generate ids in range larger than the max id in the API
        return random.randint(201, max_int32)

    @staticmethod
    def generate_book_publish_date():
        now_utc = datetime.now(timezone.utc)
        time_formatted = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
        return time_formatted