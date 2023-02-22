from django.urls import path
from . import views

urlpatterns = [
    path('child_or_pet_in_car/', views.child_or_pet_in_car),
    path('turn_on_airconditioner/', views.turn_on_airconditioner),
    path('emergency/', views.emergency),
    path('save_user_info/', views.save_user_info),
]