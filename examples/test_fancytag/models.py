# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from fancytag.models import FancyAjaxTagMixin, FancyTaggableManager


class PlanTag(FancyAjaxTagMixin, models.Model):
    text = models.TextField()
    tags = FancyTaggableManager(blank=True)


class AjaxTag(FancyAjaxTagMixin, models.Model):
    text = models.TextField()
