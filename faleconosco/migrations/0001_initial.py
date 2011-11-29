# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contato'
        db.create_table('faleconosco_contato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=60)),
            ('mensagem', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('faleconosco', ['Contato'])


    def backwards(self, orm):
        
        # Deleting model 'Contato'
        db.delete_table('faleconosco_contato')


    models = {
        'faleconosco.contato': {
            'Meta': {'object_name': 'Contato'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensagem': ('django.db.models.fields.TextField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['faleconosco']
