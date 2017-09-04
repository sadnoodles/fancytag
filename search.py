#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from django.db.models import Q


def replace_zh_chars(s):

    d = {
        u"，": ',',
        u"：": ':',
        u"”": '"',
        u"“": '"',
    }

    r = u''
    for i in s:
        r += d.get(i, i)

    return r


def spilt_search_term(search_term):
    search_term = replace_zh_chars(search_term)
    return search_term.split(" ")


def search_filter_factory(prefix, handlefunc, aliase=None):

    def search_term(queryset, segmts):
        if not segmts:
            return queryset, segmts
        left = []
        for seg in segmts:
            if not seg:
                continue
            reverse = False
            if seg[0] == '-':
                reverse = True
                rseg = seg[1:]
            elif seg[0] == '+':
                rseg = seg[1:]
            else:
                rseg = seg
            if rseg.startswith(prefix):
                terms = rseg[len(prefix):]
                queryset = handlefunc(queryset, terms, reverse)
            elif aliase and rseg.startswith(aliase):
                terms = rseg[len(aliase):]
                queryset = handlefunc(queryset, terms, reverse)
            else:
                left.append(seg)
        return queryset, left
    return search_term


def filter_tags(queryset, tag_terms, reverse):
    if not tag_terms:
        q = Q(tags__isnull=False)
    else:
        tags = tag_terms.split(',')
        q = Q(tags__name__in=tags)

    if reverse:
        queryset = queryset.filter(~q).distinct()
    else:
        queryset = queryset.filter(q).distinct()

    return queryset


tag_filter = search_filter_factory("tag:", filter_tags, aliase='#')


def search_filter(queryset, terms, filters):
    '过滤搜索参数并返回剩余的参数, filters是search_filter_factory生成的函数。'
    segmts = spilt_search_term(terms)
    for i in filters:
        queryset, segmts = i(queryset, segmts)
    return queryset, ' '.join(segmts)
