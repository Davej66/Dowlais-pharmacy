from django.urls import path 
from . import views

urlpatterns = [
    path('', views.indexc, name='indexc'),
    path('bookingc', views.bookingc, name='bookingc'),
    path('booking-submitc', views.bookingSubmit, name='bookingSubmitc'),
    path('user-panelc', views.userPanelc, name='userPanelc'),
    path('user-updatec/<int:id>', views.userUpdatec, name='userUpdatec'),
    path('user-update-submitc/<int:id>', views.userUpdateSubmitc, name='userUpdateSubmitc'),
    path('staff-panelc', views.staffPanelc, name='staffPanelc'),
]