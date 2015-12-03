# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'File'
        db.create_table(u'Files', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('size', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('data', self.gf('django.db.models.fields.BinaryField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rpg', ['File'])


    def backwards(self, orm):
        # Deleting model 'File'
        db.delete_table(u'Files')


    models = {
        u'rpg.file': {
            'Meta': {'object_name': 'File', 'db_table': "u'Files'"},
            'data': ('django.db.models.fields.BinaryField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
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