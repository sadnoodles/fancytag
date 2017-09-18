# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from test_fancytag.models import PlanTag, AjaxTag

admin.site.register(PlanTag)
admin.site.register(AjaxTag)
