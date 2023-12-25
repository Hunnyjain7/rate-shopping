from rest_framework.response import Response


class SuccessMessageMixin:
    success_messages = {
        "create": "Data added successfully.",
        "update": "Data updated successfully.",
        "retrieve": "Detail's fetched successfully.",
        "list": "Data fetched successfully.",
        "destroy": "Data deleted successfully.",
        "partial_update": "Data updated successfully.",
    }
    error_messages = {
        "create": "Failed to add data.",
        "update": "Failed to update data.",
        "retrieve": "Failed to fetch detail.",
        "list": "Failed to fetch data.",
        "destroy": "Failed to delete data.",
        "partial_update": "Failed to partially update data.",
    }

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)  # noqa

        # Ensure that response.data is initialized as a dictionary
        if response.data is None:
            response.data = {}

        # Check if the action has a corresponding success message
        action = self.action_map.get(request.method.lower())  # noqa
        success_message = self.success_messages.get(action)
        error_message = self.error_messages.get(action)

        if (
            success_message
            and isinstance(response.data, dict)
            and isinstance(response, Response)
            and response.status_code < 400
        ):
            response.data["message"] = success_message
        elif (
            error_message
            and isinstance(response.data, dict)
            and isinstance(response, Response)
            and response.status_code >= 400
        ):
            response.data["message"] = error_message
        return response
