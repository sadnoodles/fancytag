#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from django.conf import settings

from fancytag.views import AutoCompleteTags

urlpatterns = [
    url(r'^tags/$', AutoCompleteTags.as_view(), name='tag-search'),
]
