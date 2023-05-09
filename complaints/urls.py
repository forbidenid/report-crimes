from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('complaints', views.ComplaintView)


urlpatterns = [
    path('my_complaints/', views.ComplaintList.as_view(), name='my_complaints'),
    path('api/', include(router.urls)),
    path('new/', views.RegisterComplaint.as_view(), name='new_complain'),
    path('detail/<int:pk>', views.DetailComplaints.as_view(), name='detail_complain'),
    path('', views.ListComplaints.as_view(), name='all_complain'),
]