from django.urls import path
from University_Faculty.accounts.views import StudentRegisterView, UserLogoutView, UserLoginView

urlpatterns = (
    path('register/', StudentRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login')
)
