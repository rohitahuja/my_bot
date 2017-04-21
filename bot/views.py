import json
from django.http import (
    HttpResponse,
    HttpResponseForbidden,
)
from django.views.decorators.csrf import csrf_exempt
from .message import handle_entries


@csrf_exempt
def webhook(request):
    """webhook

    Router function for handling messenger events.
    """
    if request.method == 'POST':
        # Handle the message payload
        payload = json.loads(request.body)
        handle_entries(payload)

        # Notify success
        return HttpResponse("Request successful.")
    else:
        # Connecting webhook, must verify token
        if request.GET.get("hub.verify_token", "") == "johnharvard":
            response = request.GET["hub.challenge"]
            return HttpResponse(response)

        # Otherwise, user not allowed here
        return HttpResponseForbidden("You're not supposed to be here!")
