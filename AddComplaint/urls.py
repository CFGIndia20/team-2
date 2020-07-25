from django.urls import path
from AddComplaint import views

urlpatterns = [
    path('createComplaint/', views.createComplaint.as_view(), name= "complaintCreated"),
    path('retreive/', views.updateComplaint.as_view(), name='RetreiveUpdateDestroy')
]
