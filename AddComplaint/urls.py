from django.urls import path
from AddComplaint import views

urlpatterns = [
    path('createComplaint/', views.createComplaint.as_view(), name= "complaintCreated"),
    path('retreive/<int:pk>', views.updateComplaint.as_view(), name='RetreiveUpdateDestroy'),
]
