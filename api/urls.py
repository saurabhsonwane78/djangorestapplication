from django.urls import include, path
from . import views

urlpatterns = [
  path('posts', views.posts),
  path('posts/<int:post_id>', views.deleteupdateposts),
]