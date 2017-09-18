# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from fancytag.search import search_filter, tag_filter
# Register your models here.


class SearchTagMixin(object):

    def get_search_results(self, request, queryset, search_term):
        queryset, left = search_filter(
            queryset, search_term, [tag_filter])
        return super(SearchTagMixin, self).get_search_results(
            request, queryset, ' '.join(left))
