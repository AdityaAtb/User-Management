from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:id>', views.get_user_by_id, name='get_user_by_id'),
    path('users', views.get_all_users, name='get_all_users'),
    path('user', views.add_new_user, name='add_new_user'),
    path('user/update/<int:id>', views.update_user, name='update_user'),
    path('user/delete/<int:id>', views.delete_user, name='delete_user'),
]