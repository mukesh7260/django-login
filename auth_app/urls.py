from django.urls import path

# from . import views
from auth_app import views

urlpatterns=[
    path('suv/',views.sign_up_view,name='signup_url'), # suv means signup
    path('siv/',views.sign_in_view,name='signin_url'), # siv means signin
    path('sov/',views.sign_out_view,name='signout_url') # sov means signout
]