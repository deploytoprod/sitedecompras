# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Contato.mensagem2'
        db.add_column('faleconosco_contato', 'mensagem2', self.gf('django.db.models.fields.TextField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Contato.mensagem2'
        db.delete_column('faleconosco_contato', 'mensagem2')


    models = {
        'faleconosco.contato': {
            'Meta': {'object_name': 'Contato'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensagem': ('django.db.models.fields.TextField', [], {}),
            'mensagem2': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['faleconosco']
