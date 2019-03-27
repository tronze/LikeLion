from django.urls import path

from .views import AssignmentView, AssignmentDetailView, AssignmentSubmitView, AssignmentSubmitImageView, \
    SubmitUpdateView, SubmitDeleteView, TotalAssignmentSubmitView

# Create your path here.
urlpatterns = [
    path('', AssignmentView.as_view(), name='assignment-main'),
    path('<pk>/detail/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('<pk>/submit/', AssignmentSubmitView.as_view(), name='assignment-submit'),
    path('<pk>/submit_total/', TotalAssignmentSubmitView.as_view(), name='assignment-submit-total'),
    path('<pk>/submit/image/', AssignmentSubmitImageView.as_view(), name='assignment-submit-image'),
    path('update/<pk>/', SubmitUpdateView.as_view(), name='assignment-submit-update'),
    path('delete/<pk>/', SubmitDeleteView.as_view(), name='assignment-submit-delete'),
]
