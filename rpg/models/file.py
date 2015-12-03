from __future__ import unicode_literals
import os
from django.conf import settings
from django.db import models
from django.conf import settings
from django.db.models import ForeignKey
from django.db.models.fields import (
    AutoField,
    CharField,
    IntegerField,
    DecimalField,
    BinaryField,
    DateTimeField
)
from rpg import util
from rpg.util import images

# class FileTypes:
#     Image = "image"
#     Text = "text"
#     Binary = "binary"
#
#     @staticmethod
#     def table():
#         tbl = FileTypes.__table__
#         if not tbl:
#             tbl = {}
#             types = dir(FileTypes)
#             for type in types:
#                 tbl[type.lower()] = type
#
#             FileTypes.__table__ = tbl
#         return tbl
#
#     @staticmethod
#     def all():
#         tbl = FileTypes.table()
#         return tbl.values()
#
#     @staticmethod
#     def get(name):
#         lst = FileTypes.all()
#         key = name.lower()
#         match = [s for s in lst if s.lower() == key]
#         if not match:
#             return "binary"
#         return match[0]



class FilePath(object):
    __root__ = None

    def __init__(self, uri, path, relative):
        self.uri = uri
        self.path = path
        self.relative = relative

    @staticmethod
    def root():
        uri = FilePath.__root__
        if not uri:
            path = os.path.abspath(os.path.join(settings.WORKSPACE, "files"))
            uri = (path, "%s/files" % settings.URI)
            FilePath.__root__ = uri
        return uri

    @staticmethod
    def resolve(target, *type):
        target = target if isinstance(target, basestring) else target.uri
        root = FilePath.root()
        path, uri = root[0], root[1]
        if not type:
            type = get_file_type(target)
        else:
            type = type[0]
        if target.startswith(type):
            target = target[len(type) + 2:] # strip the type folder (including trailing s)

        type = type.strip().lower()
        uri = "%s/%ss/%s" % (uri, type, target)
        path = "%s%s%ss%s%s" % (path, os.sep, type, os.sep, target)

        chain = None
        folder = os.path.dirname(path)
        while not os.path.exists(folder):
            if not chain:
                chain = []
            chain.append(folder)
            folder = os.path.dirname(folder)

        if chain:
            chain.reverse()
            for tmp_dir in chain:
                os.mkdir(tmp_dir)

        return FilePath(uri, path, "%ss/%s" % (type, target))


    @property
    def exists(self):
        return os.path.exists(self.path)


class File(models.Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Files'

    id = AutoField(primary_key=True)
    label = CharField(null=False, max_length=1000)
    uri = CharField(null=False, max_length=250)
    type = CharField(null=False, max_length=250)
    size = DecimalField(null=False, max_digits=8, decimal_places=2)
    data = BinaryField(null=False)
    date_created = DateTimeField(auto_now=True)

    @staticmethod
    def create(label, data):
        assert label, "The label is not specified!"
        assert data, "The data is not specified!"
        #assert user, "The user is not specified!"

        type = get_file_type(label)
        size = len(data)

        def randomize(name):
            parts = name.split(".")
            pfx = util.rand(9999)
            parts[len(parts) - 2] = "%s_[%s]" % (parts[len(parts) - 2], str(pfx))
            name = ".".join(parts)
            return name

        file_path = None
        label = label.strip().lower()
        while True:
            name = randomize(label) if file_path else label
            bucket = util.rand(1000)
            subbucket = util.rand(1000)
            path = "%s/%s/%s" % (str(bucket), str(subbucket), name)
            file_path = FilePath.resolve(path, type)
            if not file_path.exists:
                directory = os.path.dirname(file_path.path)
                if not os.path.exists(directory):
                    parent = os.path.dirname(directory)
                    if not os.path.exists(parent):
                        os.mkdir(parent)

                    os.mkdir(directory)
                break

        util.io.write_file(
            file_path.path,
            data,
            text=True if type == "text" else False
        )
        f = File.objects.create(
            label=label,
            uri=file_path.relative,
            type=type,
            size=size,
            data=data
        )
        return f

    @staticmethod
    def get(key):
        if isinstance(key, basestring):
            if key.isdigit():
                key = int(key)

        results = File.objects.filter(pk=key) if isinstance(key, int) else File.objects.filter(uri=key)
        file = None if not results else results[0]
        if file:
            path = file.path
            if not path.exists:
                util.io.write_file(path.path, file.data, text=True if file.type == "doc" else False)
        return file

    @property
    def path(self):
        return FilePath.resolve(self.uri, self.type)

    @property
    def is_image(self):
        return True if self.type == "image" else False

    def get_path_for_size(self, size):
        parts = self.uri.split(".")
        parts[len(parts) - 2] = "%s_%s" % (parts[len(parts) - 2], size)
        name = ".".join(parts)
        name = "/".join(name.split("/")[1:]) # temporary hack
        return name

    def thumbnail(self):
        if not self.is_image:
            return None

        name = self.get_path_for_size("thumb")
        fp = FilePath.resolve(name, self.type)
        if not fp.exists:
            original = self.path.path
            images.create_thumb(original, fp.path)

        return fp

    def medium(self):
        if not self.is_image:
            return None

        name = self.get_path_for_size("medium")
        fp = FilePath.resolve(name, self.type)
        if not fp.exists:
            original = self.path.path
            images.create_medium(original, fp.path)

        return fp


    def __repr__(self):
        return "%s - %s" % (self.label, self.uri)

    def __str__(self):
        return self.__repr__()


def get_file_type(name):
    return "image"
