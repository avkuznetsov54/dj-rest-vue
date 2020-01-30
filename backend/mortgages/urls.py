from django.urls import path, include
from .views import MortgageProgramsView


app_name = 'mortgages'
urlpatterns = [
    path('all/', MortgageProgramsView.as_view()),
]
