import json
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


class PageNotFoundMiddleware(object):
    """
    This middleware class is used to handle the error page not found.

    :param object:
    :type object: object
    :returns: JSON response with status code 404.
    :rtype: dict
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (
            response.status_code == 404
            and "application/json" not in response["content-type"]
        ):
            data = {"Error": f"This url {request.path} not found."}

            response = HttpResponse(
                json.dumps(data), content_type="application/json", status=404
            )
        return response
