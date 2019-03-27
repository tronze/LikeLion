from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from assignment.models import Assignment, Submit, SubmitImage, AssignmentSubmitTotal


# Create your views here.


class AssignmentView(LoginRequiredMixin, TemplateView):
    template_name = 'assignment/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignments = Assignment.objects.filter(open=True).order_by('due_date')
        context['assignments'] = assignments.filter(due_date__gt=timezone.localtime())
        context['timeup_assignments'] = assignments.filter(due_date__lte=timezone.localtime())
        context['submit_count'] = Submit.objects.filter(author=self.request.user).values_list('assignment', flat=True).distinct().count()
        return context


class AssignmentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'assignment/detail.html'
    model = Assignment
    context_object_name = 'assignment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submits'] = AssignmentSubmitTotal.objects.filter(assignment=self.get_object(), author=self.request.user)
        context['timeup'] = self.get_object().due_date < timezone.localtime()
        return context


class AssignmentSubmitView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/create.html'
    model = Submit
    fields = ('title', 'language', 'content',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignment'] = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        context['timeup'] = True
        return context

    def form_valid(self, form):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.instance.assignment = assignment
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        if assignment.due_date > timezone.localtime():
            return super().post(request, *args, **kwargs)
        else:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context['msg'] = (False, '제출 가능한 시간이 아닙니다.')
            return self.render_to_response(context)

    def get_success_url(self):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        return reverse_lazy('assignment-detail', kwargs={'pk': assignment.pk})


class AssignmentSubmitImageView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/create_image.html'
    model = SubmitImage
    fields = ('title', 'image',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignment'] = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        context['timeup'] = True
        return context

    def form_valid(self, form):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.instance.assignment = assignment
        form.instance.language = 6
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        if assignment.due_date > timezone.localtime():
            return super().post(request, *args, **kwargs)
        else:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context['msg'] = (False, '제출 가능한 시간이 아닙니다.')
            return self.render_to_response(context)

    def get_success_url(self):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        return reverse_lazy('assignment-detail', kwargs={'pk': assignment.pk})


class SubmitUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'assignment/update.html'
    model = AssignmentSubmitTotal
    fields = ('image', 'link',)
    context_object_name = 'submit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignment'] = self.get_object().assignment
        context['timeup'] = True
        return context

    def get_success_url(self):
        return reverse_lazy('assignment-detail', kwargs={'pk': self.get_object().assignment.pk})


class SubmitDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'assignment/delete.html'
    model = AssignmentSubmitTotal
    context_object_name = 'submit'

    def delete(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            self.object = self.get_object()
            context = self.get_context_data(self.object)
            context['msg'] = (False, '권한이 없습니다.')
            self.render_to_response(context)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('assignment-detail', kwargs={'pk': self.get_object().assignment.pk})


class TotalAssignmentSubmitView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/tcreate.html'
    model = AssignmentSubmitTotal
    fields = ('image', 'link',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignment'] = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        context['timeup'] = True
        return context

    def form_valid(self, form):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.instance.assignment = assignment
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        if assignment.due_date > timezone.localtime():
            return super().post(request, *args, **kwargs)
        else:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context['msg'] = (False, '제출 가능한 시간이 아닙니다.')
            return self.render_to_response(context)

    def get_success_url(self):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        return reverse_lazy('assignment-detail', kwargs={'pk': assignment.pk})
