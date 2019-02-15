from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import TemplateView
from django.http import HttpResponseForbidden

from account.forms import UserPasswordResetForm
from account.models import RegisterLink

# Create your views here.


class MainView(TemplateView):
    template_name = ''


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        link = get_object_or_404(RegisterLink, uuid=context['uuid'])
        context['link'] = link
        context['form'] = UserPasswordResetForm()
        return context

    def get(self, request, *args, **kwargs):
        link = get_object_or_404(RegisterLink, uuid=kwargs.get('uuid'))
        if link.register_available is False or link.register_until < timezone.now():
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        context = {}
        request = self.request
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password2']
            link = get_object_or_404(RegisterLink, uuid=kwargs.get('uuid'))
            user = link.user
            user.set_password(password)
            user.save()
            link.register_available = False
            link.save()
            return render(request, 'registration/success.html', context)
        else:
            context['form'] = form
            return render(request, self.template_name, context)
