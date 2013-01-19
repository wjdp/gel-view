# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GelRef.colour_description'
        db.add_column('gel_view_gelref', 'colour_description',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GelRef.description'
        db.add_column('gel_view_gelref', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'GelRef.colour_description'
        db.delete_column('gel_view_gelref', 'colour_description')

        # Deleting field 'GelRef.description'
        db.delete_column('gel_view_gelref', 'description')


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
            'colour_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['gel_view']