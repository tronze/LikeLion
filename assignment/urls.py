from django.urls import path

from .views import AssignmentView, AssignmentDetailView, AssignmentSubmitView, SubmitDeleteView

# Create your path here.
urlpatterns = [
    path('', AssignmentView.as_view(), name='assignment-main'),
    path('<pk>/detail/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('<pk>/submit/', AssignmentSubmitView.as_view(), name='assignment-submit'),
    path('delete/<pk>/', SubmitDeleteView.as_view(), name='assignment-delete'),
]
