from rest_framework import status

def error_handler(exception):
    status_code = getattr(exception, 'status', status.HTTP_500_INTERNAL_SERVER_ERROR)
    errors = getattr(exception, 'errors', None)
    errorResponse = {'error': str(exception)}
    if errors:
        errorResponse['errors'] = errors
    return errorResponse, status_code
