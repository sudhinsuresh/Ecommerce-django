from django.urls import path
from arkauth import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.handlelogin,name="login"),
    path('logout/',views.handlelogout,name="logout"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),


]