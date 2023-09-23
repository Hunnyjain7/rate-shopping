from rest_framework.status import HTTP_200_OK

from core.constant import SUCCESS


class CustomResponse(object):
    """
    A custom response class for Django REST Framework that adds a `status`, `message`, 'error' & `data`
    attribute to the response data.
    """

    def __init__(self, status=SUCCESS, message="", error=list, data=dict, status_code=HTTP_200_OK, **kwargs):
        data = {"status": status, "message": message, "error": error, "data": data}
        super().__init__(data, status=status_code, **kwargs)
