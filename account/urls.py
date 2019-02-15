from django.urls import path, include

from .views import RegisterView

# Create your urls here.
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/<uuid>/', RegisterView.as_view(), name='register'),
]
