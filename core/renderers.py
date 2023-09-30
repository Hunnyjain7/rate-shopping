from rest_framework import status as rest_status_codes
from rest_framework.renderers import JSONRenderer

from core.constant import DATA, ERROR, FAIL, MESSAGE, SUCCESS


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context["response"]
        status_code = response.status_code
        success_status_codes = [
            rest_status_codes.HTTP_200_OK,
            rest_status_codes.HTTP_201_CREATED,
            rest_status_codes.HTTP_202_ACCEPTED,
            rest_status_codes.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            rest_status_codes.HTTP_204_NO_CONTENT,
            rest_status_codes.HTTP_205_RESET_CONTENT,
            rest_status_codes.HTTP_206_PARTIAL_CONTENT,
            rest_status_codes.HTTP_207_MULTI_STATUS,
            rest_status_codes.HTTP_208_ALREADY_REPORTED,
            rest_status_codes.HTTP_226_IM_USED,
        ]
        status = (
            data.pop(SUCCESS)
            if SUCCESS in data
            else SUCCESS
            if status_code in success_status_codes
            else FAIL
        )
        message = (
            data.pop(MESSAGE)
            if MESSAGE in data
            else "Operation successful."
            if status == SUCCESS
            else ""
        )
        error = data.pop(ERROR) if ERROR in data else dict()
        data = data.pop(DATA) if DATA in data else data
        if status_code not in success_status_codes:
            error = data
            data = dict()
        response_data = {SUCCESS: status, MESSAGE: message, ERROR: error, DATA: data}

        return super().render(response_data, accepted_media_type, renderer_context)
