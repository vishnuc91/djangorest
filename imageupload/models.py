# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    name = models.CharField('Name', max_length=150)
    image = models.ImageField('Image', upload_to='images')

    def __unicode__(self):
        return u'%s' % self.name
