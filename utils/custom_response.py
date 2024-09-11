from rest_framework.response import Response
from rest_framework import status


class ErrorResponse(Response):
    def __init__(self, data=None, status_code=None, message=None):
        response_data = {
            'code': status_code if status_code else status.HTTP_400_BAD_REQUEST,
            'data': data if data else None,
            'message': message if message else None
        }
        super().__init__(data={"error": response_data}, status=status_code)