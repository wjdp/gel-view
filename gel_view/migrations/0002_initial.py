# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GelRef'
        db.create_table('gel_view_gelref', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('colour', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
        ))
        db.send_create_signal('gel_view', ['GelRef'])

        # Adding model 'Gel'
        db.create_table('gel_view_gel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gelref', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gel_view.GelRef'])),
            ('quantity_cut', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_sheet', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gel_view', ['Gel'])


    def backwards(self, orm):
        # Deleting model 'GelRef'
        db.delete_table('gel_view_gelref')

        # Deleting model 'Gel'
        db.delete_table('gel_view_gel')


    models = {
        'gel_view.gel': {
            'Meta': {'object_name': 'Gel'},
            'gelref': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gel_view.GelRef']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity_cut': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_sheet': ('django.db.models.fields.IntegerField', [], {})
        },
        'gel_view.gelref': {
            'Meta': {'object_name': 'GelRef'},
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['gel_view']