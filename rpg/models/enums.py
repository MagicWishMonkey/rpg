from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import (
    CharField,
    IntegerField,
    AutoField
)


class Status(models.Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Status'

    id = AutoField(primary_key=True)
    label = CharField(max_length=25, null=False)

    @staticmethod
    def list():
        lst = Status.objects.all()
        return [o for o in lst]

    @classmethod
    def get(cls, name):
        key = name.strip().upper()
        lst = cls.list()
        for val in lst:
            if val.label.upper() == key:
                return val
        return None

    def __repr__(self):
        return "%s - %s" % (self.label, str(self.id))

    def __str__(self):
        return self.__repr__()


class Style(models.Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Styles'

    id = AutoField(primary_key=True)
    label = CharField(max_length=25, null=False)

    @staticmethod
    def list():
        lst = Style.objects.all()
        return [o for o in lst]

    @classmethod
    def get(cls, name):
        key = name.strip().upper()
        lst = cls.list()
        for val in lst:
            if val.label.upper() == key:
                return val
        return None

    def __repr__(self):
        return "%s - %s" % (self.label, str(self.id))

    def __str__(self):
        return self.__repr__()


class Type(models.Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Types'

    id = AutoField(primary_key=True)
    label = CharField(max_length=25, null=False)

    @staticmethod
    def list():
        lst = Type.objects.all()
        return [o for o in lst]

    @classmethod
    def get(cls, name):
        key = name.strip().upper()
        lst = cls.list()
        for val in lst:
            if val.label.upper() == key:
                return val
        return None

    def __repr__(self):
        return "%s - %s" % (self.label, str(self.id))

    def __str__(self):
        return self.__repr__()


class Plan(models.Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Plans'

    id = AutoField(primary_key=True)
    label = CharField(max_length=25, null=False)

    @staticmethod
    def list():
        lst = Plan.objects.all()
        return [o for o in lst]

    @classmethod
    def get(cls, name):
        key = name.strip().upper()
        lst = cls.list()
        for val in lst:
            if val.label.upper() == key:
                return val
        return None


    def __repr__(self):
        return "%s - %s" % (self.label, str(self.id))

    def __str__(self):
        return self.__repr__()