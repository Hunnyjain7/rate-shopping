from rest_framework.response import Response

from core.constant import SUCCESS_STATUS_CODES


class SuccessMessageMixin:
    success_messages = {
        'create': "Data added successfully.",
        'update': "Data updated successfully.",
        'retrieve': "Detail's fetched successfully.",
        'list': "Data fetched successfully.",
        'destroy': "Data deleted successfully.",
        'partial_update': "Data updated successfully."
    }

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)  # noqa

        # Ensure that response.data is initialized as a dictionary
        if response.data is None:
            response.data = {}

        # Check if the method has a corresponding success message
        method_name = self.action_map.get(request.method.lower())  # noqa
        success_message = self.success_messages.get(method_name)

        if success_message and isinstance(response, Response) and response.status_code in SUCCESS_STATUS_CODES:
            response.data['message'] = success_message

        return response
