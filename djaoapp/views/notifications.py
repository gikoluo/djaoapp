# Copyright (c) 2019, DjaoDjin inc.
# see LICENSE

from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template
from rules.mixins import AppMixin
from saas.models import get_broker

from ..api.notifications import get_test_email_context
from ..compat import reverse


class NotificationInnerFrameView(AppMixin, TemplateView):

    template_name = 'notification/detail.html'

    def get_template_names(self):
        template_name = self.kwargs.get('template', None)
        if template_name.endswith('_role_added'):
            return ["notification/%s.eml" % template_name,
                "notification/role_added.eml"]
        return ["notification/%s.eml" % template_name]

    def get_context_data(self, **kwargs):
        context = super(NotificationInnerFrameView, self).get_context_data(
            **kwargs)
        context.update(get_test_email_context())
        return context


class NotificationDetailView(AppMixin, TemplateView):

    template_name = 'notification/detail.html'

    def _get_template_names(self):
        template_name = self.kwargs.get('template', None)
        if template_name.endswith('_role_added'):
            return ["notification/%s.eml" % template_name,
                "notification/role_added.eml"]
        return ["notification/%s.eml" % template_name]

    def get_context_data(self, **kwargs):
        context = super(NotificationDetailView, self).get_context_data(**kwargs)
        contents = ''
        names = self._get_template_names()
        if names: 
            tpl = get_template(names[0])
            with open(tpl.template.template.filename) as f:
                contents = f.read()
        context.update({
            'contents': contents,
            'api_sources': reverse('pages_api_sources'),
            'iframe_url': reverse('notification_inner_frame',
                args=(self.kwargs.get('template'),))})
        return context
