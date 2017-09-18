# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import views
from rest_framework.response import Response
from taggit.models import Tag
from fancytag.serializers import TagSerializer

# Create your views here.


class AutoCompleteTags(views.APIView):

    search_param = 'q'

    def get(self, request, format=None):
        query = request.GET.get(self.search_param, None)
        if query.strip():
            res = Tag.objects.filter(name__contains=query)[:50]
        else:
            res = Tag.objects.all()[:50]

        serializer = TagSerializer(res, many=True)
        return Response(data=serializer.data)
