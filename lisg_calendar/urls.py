from django.urls import path

from . import views

# Create your urls here.
urlpatterns = [
    path('', views.display_simple_web_calendar, name='lisg-calendar-main'),
]