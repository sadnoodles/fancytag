# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager
from fancytag.widgets import TagAutoComplete, AjaxTagWidget

# Create your models here.


class FancyTaggableManager(TaggableManager):

    def formfield(self, **kwargs):
        kwargs['widget'] = TagAutoComplete
        return super(FancyTaggableManager, self).formfield(**kwargs)


class FancyAjaxTaggableManager(TaggableManager):

    def formfield(self, **kwargs):
        kwargs['widget'] = AjaxTagWidget
        return super(FancyAjaxTaggableManager, self).formfield(**kwargs)


class FancyTagMixin(models.Model):
    tags = FancyTaggableManager(blank=True)

    class Meta:
        abstract = True


class FancyAjaxTagMixin(models.Model):
    tags = FancyAjaxTaggableManager(blank=True)

    class Meta:
        abstract = True
