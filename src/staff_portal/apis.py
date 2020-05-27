from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from client_portal.models import WasteManager, Organization


@login_required
def organizations_info(request):
    clientmangager = request.user.clientmanager
    data = {
        'organizations': list(clientmangager.organizations.values())
    }
    return JsonResponse(data)


@login_required
def pending_changes(request):
    clientmangager = request.user.clientmanager
    change_requests = []
    for e in clientmangager.organizations.get_queryset().all():
        change_requests_particular = list(e.changerequest_set.values())
        for change_request in change_requests_particular:
            change_request['wastemanager'] = WasteManager.objects.get(pk=change_request['wastemanager_id']).user.first_name
            change_request['organization'] = Organization.objects.get(pk=change_request['organization_id']).name
        change_requests.append(change_requests_particular)
    data = {
        'change_requests': change_requests
    }
    return JsonResponse(data)


