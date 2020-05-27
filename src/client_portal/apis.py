from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def wastemanager(request):
    print(dir(request.user.wastemanager))
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)