from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from metrics.logger import log
from rpg import util



def authenticate(func):
    enabled = False
    def inner(*args, **kwargs):
        request = args[0]
        if not request.user.id and enabled:
            if request.path.lower().startswith("/api/"):
                return View(request).write(
                    {"error": "You do not have permission to access this resource."},
                    status=403
                )

            return View(request).render("unauthorized.html")
        return func(*args, **kwargs)
    return inner


class View(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session

    def login(self):
        # from accounts.models import BalanceUser as User
        # from django.contrib.auth import login as auth_login

        # user = User()
        # user.email = email
        # user.set_password(password)
        # user.activation_token = util.guid()
        # user.is_active = True
        # user.activation_token = "" # Nullify activation_token
        # user.save()
        #
        # auth_login(request, user)
        # self.session.set_expiry(7200)
        return True

    def render(self, template, **kwargs):
        return render_to_response(
            template,
            kwargs,
            context_instance=RequestContext(self.request)
        )

    def write(self, data, **kwargs):
        content_type = kwargs.get('content-type', 'text/html')
        if isinstance(data, (dict, list)):
            content_type = 'application/json'
            data = util.json(data)

        status = kwargs.get("status", 200)
        return HttpResponse(data, content_type=content_type, status=status)

