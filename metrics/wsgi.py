"""
WSGI config for metrics project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metrics.settings")

application = get_wsgi_application()


# from rpg import util
# from rpg.models import File
# from PIL import Image
#
#
# f = File.get(5)
# m = f.medium()
# thumb = f.thumbnail()
# f2 = File.get('images/527/249/butters.jpg')
# data = util.io.read_file("/Users/ron/Dropbox/small-ron.png", text=False)
# file = File.create("butters.jpg", data)
# thumb = file.thumbnail()
# # for x in xrange(100):
# #     print util.rand(100)
#
# print ""
