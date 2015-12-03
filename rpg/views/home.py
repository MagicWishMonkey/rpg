from .view import *


def get(request):
    return View(request).render("home.html")
