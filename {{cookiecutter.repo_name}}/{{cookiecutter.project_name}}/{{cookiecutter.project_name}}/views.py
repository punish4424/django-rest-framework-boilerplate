from django.http import JsonResponse

from rest_framework import status


def handler404(request, exception):
    data = {
        'errors': {'not_found': 'This URL does not exist'},
        'status': False,
        'status_code': status.HTTP_404_NOT_FOUND

    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


def handler500(request):
    data = {
        'error': {'server_error': 'Server Error (500)'},
        'status': False,
        'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
