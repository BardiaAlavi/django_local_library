from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static

app_name='Posts'

urlpatterns = [
    path('', views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
    path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
