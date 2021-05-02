from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.patient_form,name='patient_insert'), # get and post req. for insert operation
    path('<int:id>/', views.patient_form,name='patient_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.patient_delete,name='patient_delete'),
    path('list/',views.patient_list,name='patient_list') # get req. to retrieve and display all records
]