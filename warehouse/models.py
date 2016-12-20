from __future__ import unicode_literals

from django.db import models

class TestScrapy(models.Model):
    text= models.CharField(max_length=255)
    author= models.CharField(max_length=255)

    class Meta:
        app_label = 'warehouse'
        db_table = 'test_scrapy'