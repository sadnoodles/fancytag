# -*- coding: utf-8 -*-

import json
from django import forms
from django.forms import Media
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils import six
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from taggit.models import Tag


class TagAutoComplete(forms.TextInput):
    """
    Tag widget with autocompletion based on select2.
    """

    def __init__(self, attrs=None):
        final_attrs = {'class': 'vTextField'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(TagAutoComplete, self).__init__(attrs=final_attrs)

    @property
    def get_tags(self):
        """
        Returns the list of tags to auto-complete.
        """
        return [tag.name for tag in
                Tag.objects.all()[:50]]

    def get_js(self, id_name):
        return """
<script type="text/javascript">
fancytag_static("#id_%(id_name)s", %(tag_list)s);
</script>""" % dict(
            tag_list=json.dumps(self.get_tags),
            id_name=id_name)

    def render(self, name, value, attrs=None):
        """
        Render the default widget and initialize select2.
        """
        # print name, value, attrs
        if value is None:
            value = ""
        elif isinstance(value, six.string_types):
            pass
        else:
            value = ', '.join(
                [o.tag.name for o in value.select_related("tag")])

        output = [super(TagAutoComplete, self).render(name, value, attrs)]
        output.append(self.get_js(name))
        return mark_safe('\n'.join(output))

    @property
    def media(self):
        """
        TagAutoComplete's Media.
        """
        def static(path):
            return staticfiles_storage.url(
                'admin/select2/%s' % path)
        return Media(
            css={'all': (static('css/select2.css'),)},
            js=(static('js/select2.js'),
                staticfiles_storage.url('admin/js/fancytag.js'))
        )


class AjaxTagWidget(TagAutoComplete):
    url_path = ''

    def get_js(self, id_name):
        return """
<script type="text/javascript">
fancytag("#id_%(id_name)s", "%(api_url)s");
</script>""" % dict(
            api_url=self.url_path or reverse("fancytag:tag-search"),
            id_name=id_name)
