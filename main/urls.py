from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('results/<int:election>/', ResultsView.as_view(), name="results"),
    path('configuration/', ConfigurationView.as_view(), name="configuration")
]
