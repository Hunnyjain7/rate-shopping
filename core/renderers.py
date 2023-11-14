from rest_framework.renderers import JSONRenderer
from core.constant import DATA, ERROR, FAIL, MESSAGE, STATUS, SUCCESS, SUCCESS_STATUS_CODES


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context["response"]
        response_data = self.get_response_data(data, response)
        return super().render(response_data, accepted_media_type, renderer_context)

    @staticmethod
    def get_response_data(data, response):
        status_code = response.status_code
        status = (
            data.pop(SUCCESS)
            if SUCCESS in data
            else SUCCESS
            if status_code in SUCCESS_STATUS_CODES
            else FAIL
        )
        message = (
            data.pop(MESSAGE)
            if MESSAGE in data
            else "Data fetched successfully."
            if status == SUCCESS
            else "Operation failed."
        )
        error = data.pop(ERROR) if ERROR in data else dict()
        data = data.pop(DATA) if DATA in data else data
        if not error and status_code not in SUCCESS_STATUS_CODES:
            error = data
            data = dict()
        return {STATUS: status, MESSAGE: message, ERROR: error, DATA: data}
