from django.urls import path

urlpatterns = [
    path('createComplaint/', views.createComplaint.as_view(), name= "complaintCreated")
]
