import os
import io
from PIL import Image
from django.conf import settings



def create_thumb(image, *output):
    size = settings.IMAGE_SIZES["THUMB"]
    return resize(image, size["width"], size["height"], *output)


def create_medium(image, *output):
    size = settings.IMAGE_SIZES["MEDIUM"]
    return resize(image, size["width"], size["height"], *output)


def create_large(image, *output):
    size = settings.IMAGE_SIZES["LARGE"]
    return resize(image, size["width"], size["height"], *output)


def resize(image, width, height, *output):
    img = None
    if isinstance(image, basestring):
        if os.path.exists(image):
            img = Image.open(image)

    if not img:
        buffer = io.BytesIO(image)
        img = Image.open(buffer)
        buffer.close()

    format = "JPEG"
    img.thumbnail((width, height))
    if not output:
        output = io.BytesIO()
        img.save(output, format=format)
        data = output.getvalue()
        output.close()
        return data

    output = output[0]
    img.save(output, format)

