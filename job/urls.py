from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.job_list),      # نخلي ده الاساسي
    path('<int:id>', views.job_details),   # id ينده كل وظيفه ب ال      to easily filter each job    in views.py
    
]