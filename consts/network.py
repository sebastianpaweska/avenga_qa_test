from enum import Enum

class Network(Enum):
    API_URL = "fakerestapi.azurewebsites.net"
    PROTOCOL = "https"

    # endpoints
    BOOKS = "/api/v1/Books"
    AUTHORS = "/api/v1/Authors"
