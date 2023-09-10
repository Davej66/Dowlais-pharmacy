from django.urls import path 
from . import views

urlpatterns = [
    path('', views.indexa, name='indexa'),
    path('bookinga', views.bookinga, name='bookinga'),
    path('booking-submita', views.bookingSubmit, name='bookingSubmita'),
    path('user-panela', views.userPanela, name='userPanela'),
    path('user-updatea/<int:id>', views.userUpdatea, name='userUpdatea'),
    path('user-update-submita/<int:id>', views.userUpdateSubmita, name='userUpdateSubmita'),
    path('staff-panela', views.staffPanela, name='staffPanela'),
]