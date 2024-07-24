from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('records/', views.records.as_view(), name='records'),
    path('record/<int:pk>/',views.record.as_view(), name='record-detail'),
    path('login/', views.loginUser.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.rgisterUser.as_view(), name='signup'),
    path('add-record/', views.recordCreation.as_view(),name='add-record'),
    path('edit-record/<int:pk>/', views.updateRecord, name='edit-record'),
    path('delete-record/<int:pk>/',views.deleteRecord, name='delete-record'),



    # path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    # path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]