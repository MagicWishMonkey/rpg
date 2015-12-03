from ..view import *


@authenticate
def select(request):
    return View(request).write(
        [{"label": "5200 Winedale"}, {"label": "1234 Evergreen Terrace"}]
    )



