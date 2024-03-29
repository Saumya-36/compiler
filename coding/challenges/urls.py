# challenges/urls.py
from django.urls import path
from .views import challenge_list, challenge_detail, submit_code

urlpatterns = [
    path('list/', challenge_list, name='challenge_list'),
    path('<int:challenge_id>/', challenge_detail, name='challenge_detail'),
    path('submit_code/<int:challenge_id>/', submit_code, name='submit_code'),
]
