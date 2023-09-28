from django.urls import path 
from . import views

urlpatterns = [
    path('', views.indexb, name='indexb'),
    path('bookingb', views.bookingb, name='bookingb'),
    path('booking-submitb', views.bookingSubmit, name='bookingSubmitb'),
    path('user-panelb', views.userPanelb, name='userPanelb'),
    path('user-updateb/<int:id>', views.userUpdateb, name='userUpdateb'),
    path('user-update-submitb/<int:id>', views.userUpdateSubmitb, name='userUpdateSubmitb'),
    path('staff-panelb', views.staffPanelb, name='staffPanelb'),
]