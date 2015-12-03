# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def populate(self):
        from django.core.management import call_command

        call_command("loaddata", "statuses.json")
        call_command("loaddata", "styles.json")
        call_command("loaddata", "types.json")


    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table(u'Types', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'rpg', ['Type'])

        # Adding model 'Plan'
        db.create_table(u'Plans', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'rpg', ['Plan'])

        # Adding model 'Status'
        db.create_table(u'Status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'rpg', ['Status'])

        # Adding model 'Style'
        db.create_table(u'Styles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'rpg', ['Style'])
        self.populate()

    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table(u'Types')

        # Deleting model 'Plan'
        db.delete_table(u'Plans')

        # Deleting model 'Status'
        db.delete_table(u'Status')

        # Deleting model 'Style'
        db.delete_table(u'Styles')


    models = {
        u'rpg.plan': {
            'Meta': {'object_name': 'Plan', 'db_table': "u'Plans'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'rpg.status': {
            'Meta': {'object_name': 'Status', 'db_table': "u'Status'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'rpg.style': {
            'Meta': {'object_name': 'Style', 'db_table': "u'Styles'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'rpg.type': {
            'Meta': {'object_name': 'Type', 'db_table': "u'Types'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['rpg']