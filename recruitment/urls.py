from django.contrib.auth.decorators import login_required
from django.urls import path

from recruitment.views import ApplicantListView, ApplicationListView, ApplicantDetailView, ApplicationDetailView, \
    RecruitmentMainView

# Create your urls here.


urlpatterns = [
    path('', login_required(RecruitmentMainView.as_view()), name='recruitment-main'),
    path('applicants/', login_required(ApplicantListView.as_view()), name='recruitment-applicants-list'),
    path('applicants/<pk>/', login_required(ApplicantDetailView.as_view()), name='recruitment-applicants-detail'),
    path('applications/', login_required(ApplicationListView.as_view()), name='recruitment-applications-list'),
    path('applications/<pk>/', login_required(ApplicationDetailView.as_view()), name='recruitment-applications-detail'),
]
