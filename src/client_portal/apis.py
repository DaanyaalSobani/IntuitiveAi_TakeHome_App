from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def wastemanager_info(request):
    wastemanager = request.user.wastemanager
    data = {
        'name': wastemanager.user.first_name,
        'organization': wastemanager.organization.name
    }
    return JsonResponse(data)

@login_required
def trash_info(request):
    organization = request.user.wastemanager.organization
    data = {
        'trash': list(organization.trash_set.values())
    }
    return JsonResponse(data)