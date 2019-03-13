from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView

from recruitment.controller import EvaluationController
from recruitment.models import Applicant, Application, ApplicantApplication, Evaluation, \
    AnswerEvaluation, EvaluationQuestion, Interviewee


# Create your views here.


class RecruitmentMainView(PermissionRequiredMixin, TemplateView):
    template_name = 'recruitment/main.html'
    permission_required = ['recruitment.view_applicationevaluation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "모집"
        context['application'] = Evaluation.get_application()
        context['application_count'] = Evaluation.get_application_count()
        evaluation_controller = EvaluationController(context['application'], self.request.user)
        evaluation_controller.process_evaluated_check()
        context['evaluations'] = evaluation_controller.get_application_evaluation_states()
        context['accepted'] = Interviewee.objects.filter(accepted=True)
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


class EvaluationView(PermissionRequiredMixin, TemplateView):
    template_name = 'recruitment/evaluation/main.html'
    permission_required = 'recruitment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = Evaluation.get_application()
        evaluation_controller = EvaluationController(application, self.request.user)
        evaluation_controller.process_evaluated_data()
        context['title'] = '지원서 평가'
        context['evaluation_controller'] = evaluation_controller
        return context


class EvaluationDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'recruitment/evaluation/main.html'
    model = ApplicantApplication
    permission_required = ['recruitment.view_applicantapplication','recruitment.add_applicantapplication', 'recruitment.change_applicantapplication']
    context_object_name = 'applicant_application'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.get_object().pk
        application = Evaluation.get_application()
        evaluation_controller = EvaluationController(application, self.request.user)
        evaluation_controller.process_evaluated_data()
        application_evaluation, created = self.get_object().applicationevaluation_set.get_or_create(
            user=self.request.user, application=self.get_object(), evaluation=Evaluation.get_active_evaluation())
        evaluation_question, created = EvaluationQuestion.objects.get_or_create(
            application_evaluation=application_evaluation)
        context['title'] = '지원서 평가'
        context['pk'] = pk
        context['evaluation_controller'] = evaluation_controller
        context['evaluation_question'] = evaluation_question.question
        return context

    def post(self, *args, **kwargs):
        query_dict = self.request.POST
        application = Evaluation.get_application()
        evaluation_controller = EvaluationController(application, self.request.user)
        questions = evaluation_controller.get_questions()
        applicant_application = self.get_object()
        application_evaluation, created = applicant_application.applicationevaluation_set.get_or_create(user=self.request.user, application=applicant_application, evaluation=Evaluation.get_active_evaluation())
        for question in questions:
            score = query_dict.get(str(question.order))
            answer_evaluation, created = AnswerEvaluation.objects.get_or_create(answer=question.answer_set.get(applicant=applicant_application.get_applicant()), application_evaluation=application_evaluation)
            if score is '':
                score = 0
            answer_evaluation.score = score
            answer_evaluation.save()
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['msg'] = (True, '성공적으로 저장되었습니다.')
        return self.render_to_response(context)


class EvaluationQuestionView(PermissionRequiredMixin, DetailView):
    template_name = 'recruitment/evaluation/main.html'
    model = ApplicantApplication
    permission_required = ['recruitment.view_applicantapplication','recruitment.add_applicantapplication', 'recruitment.change_applicantapplication', 'recruitment.view_evaluationquestion', 'recruitment.add_evaluationquestion', 'recruitment.change_evaluationquestion']
    context_object_name = 'applicant_application'

    def post(self, *args, **kwargs):
        query_dict = self.request.POST
        applicant_application = self.get_object()
        application_evaluation, created = applicant_application.applicationevaluation_set.get_or_create(user=self.request.user, application=applicant_application, evaluation=Evaluation.get_active_evaluation())
        question = query_dict.get('question')
        evaluation_question, created = EvaluationQuestion.objects.get_or_create(application_evaluation=application_evaluation)
        evaluation_question.question = question
        evaluation_question.save()
        return redirect('recruitment-evaluation-detail', pk=self.get_object().pk)
