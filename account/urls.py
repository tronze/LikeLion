from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import RegisterView, MyView, MentorMenteeView, MentorMenteeDetailView

# Create your urls here.
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/<uuid>/', RegisterView.as_view(), name='register'),
    path('profile/', login_required(MyView.as_view()), name='profile'),
    path('mentor_mentee/', MentorMenteeView.as_view(), name='mentor-mentee-main'),
    path('mentor_mentee/detail/', MentorMenteeDetailView.as_view(), name='mentor-mentee-detail'),
]
