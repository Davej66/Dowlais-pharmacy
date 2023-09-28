from django.urls import path 
from . import views

urlpatterns = [
    path('', views.indexd, name='indexd'),
    path('bookingd', views.bookingd, name='bookingd'),
    path('booking-submitd', views.bookingSubmit, name='bookingSubmitd'),
    path('user-paneld', views.userPaneld, name='userPaneld'),
    path('user-updated/<int:id>', views.userUpdated, name='userUpdated'),
    path('user-update-submitd/<int:id>', views.userUpdateSubmitd, name='userUpdateSubmitd'),
    path('staff-paneld', views.staffPaneld, name='staffPaneld'),
]