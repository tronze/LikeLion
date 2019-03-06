from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView

from recruitment.models import Applicant, Application, ApplicantApplication


# Create your views here.


class RecruitmentMainView(PermissionRequiredMixin, TemplateView):
    template_name = 'recruitment/main.html'
    permission_required = 'recruitment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "모집"
        context['applicant_count'] = Applicant.objects.count()
        context['application_count'] = ApplicantApplication.objects.count()
        return context


class ApplicantListView(PermissionRequiredMixin, ListView):
    template_name = 'recruitment/applicant/list.html'
    model = Applicant
    permission_required = 'recruitment.view_applicant'
    context_object_name = 'applicants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "모집 지원자 정보"
        return context


class ApplicantDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'recruitment/applicant/detail.html'
    model = Applicant
    permission_required = 'recruitment.view_applicant'
    context_object_name = 'applicant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "%s님 지원 정보" % self.get_object().name
        return context


class ApplicationListView(PermissionRequiredMixin, ListView):
    template_name = 'recruitment/application/list.html'
    model = Application
    permission_required = 'recruitment.view_application'
    context_object_name = 'applications'


class ApplicationDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'recruitment/application/detail.html'
    model = Application
    permission_required = 'recruitment.view_application'
    context_object_name = 'application'
