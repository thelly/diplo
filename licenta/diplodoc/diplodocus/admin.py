'''
Created on Jul 2, 2012

@author: Vlad Posea (http://vlad.posea.eu)
'''
from django.contrib import admin
from diplodocus.models import Article
from django import forms
from django.db import models

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
        
admin.site.register(Article,ArticleAdmin)