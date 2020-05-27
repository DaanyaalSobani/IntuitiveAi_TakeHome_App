from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def organizations_info(request):
    clientmangager = request.user.clientmanager
    data = {
        'organizations': list(clientmangager.organizations.values())
    }
    return JsonResponse(data)


