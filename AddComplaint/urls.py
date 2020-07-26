from django.urls import path
from AddComplaint import views
from .views import index

urlpatterns = [
    path('createComplaint/', views.createComplaint.as_view(), name= "complaintCreated"),
    path('retreive/<int:pk>', views.updateComplaint.as_view(), name='RetreiveUpdateDestroy'),
    path('send_complain/createComplaint/', views.createComplaint.as_view(), name= "complaintCreated"),
    path('send_complain/', views.complain),
    path('/index', index, name= "index"),

]
