from rest_framework import status

ADMIN = "Admin"
CLIENT = "Client"
GROUPS = {"Admin": ADMIN, "Client": CLIENT}
STATUS = "status"
SUCCESS = "success"
FAIL = "fail"
ERROR = "error"
MESSAGE = "message"
DATA = "data"
SYSTEM = "system"
SUCCESS_STATUS_CODES = [
    status.HTTP_200_OK,
    status.HTTP_201_CREATED,
    status.HTTP_202_ACCEPTED,
    status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
    status.HTTP_204_NO_CONTENT,
    status.HTTP_205_RESET_CONTENT,
    status.HTTP_206_PARTIAL_CONTENT,
    status.HTTP_207_MULTI_STATUS,
    status.HTTP_208_ALREADY_REPORTED,
    status.HTTP_226_IM_USED,
]
