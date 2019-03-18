import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from django.http import HttpResponseForbidden

from account.forms import UserPasswordResetForm
from account.models import RegisterLink, User

# Create your views here.
from main_calendar.web_calendar import WebCalendar
from recruitment.models import Interviewee


class MainView(TemplateView):
    template_name = ''


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        link = get_object_or_404(RegisterLink, uuid=context['uuid'])
        context['title'] = "회원가입"
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
        link = get_object_or_404(RegisterLink, uuid=kwargs.get('uuid'))
        request = self.request
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password2']
            user = link.user
            user.set_password(password)
            user.save()
            link.register_available = False
            link.save()
            return render(request, 'registration/success.html', context)
        else:
            context['title'] = "회원가입"
            context['link'] = link
            context['form'] = form
            return render(request, self.template_name, context)


class MyView(TemplateView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.localdate()
        year = today.year
        month = today.month
        web_calendar = WebCalendar(year, month)
        web_calendar.set_today(year, month, today.day)
        context['title'] = "마이페이지"
        context['info'] = mark_safe(web_calendar.get_info_div().create_element())
        context['calendar'] = mark_safe(web_calendar.get_calendar_table())
        return context


class MentorMenteeView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'mentor/main.html'
    permission_required = 'recruitment.view_interviewee'


class MentorMenteeDetailView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'mentor/detail.html'
    permission_required = 'recruitment.view_interviewee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interviewees = list(Interviewee.objects.filter(accepted=True))
        mentors = list(User.objects.filter(is_staff=True))

        u1 = User.objects.filter(name='신유라')
        u2 = User.objects.filter(name='조선미')

        success = False

        while not success:
            results = self.shuffle_mentor_mentee(interviewees=interviewees, mentors=mentors)

            i1 = results[0]
            i2 = results[1]
            i3 = results[2]
            i4 = results[3]

            if u1 in i1 and u2 in i1:
                continue
            if u1 in i2 and u2 in i2:
                continue
            if u1 in i3 and u2 in i3:
                continue
            if u1 in i4 and u2 in i4:
                continue

            success = True

        context['i1'] = i1
        context['i2'] = i2
        context['i3'] = i4
        context['i4'] = i3
        return context

    @staticmethod
    def shuffle_mentor_mentee(interviewees, mentors):
        random.shuffle(interviewees)
        random.shuffle(mentors)
        i1 = list(interviewees[:4])
        i1.append(mentors[:2])
        mentors = mentors[2:]
        interviewees = interviewees[4:]
        i2 = list(interviewees[:5])
        i2.append(mentors[:2])
        mentors = mentors[2:]
        interviewees = interviewees[5:]
        i3 = list(interviewees[:5])
        i3.append(mentors[:2])
        mentors = mentors[2:]
        interviewees = interviewees[5:]
        i4 = list(interviewees[:5])
        i4.append(mentors[:2])
        return i1, i2, i3, i4
