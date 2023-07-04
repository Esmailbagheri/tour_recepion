from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/detail/<int:post_id>/<slug:post_slug>', views.HomeDetailView.as_view(), name='detail_home'),
    path('post/delete/<int:post_id>', views.DeletePostView.as_view(), name='delete_post'),
    path('post/update/<int:post_id>', views.UpdatePostView.as_view(), name='update_post'),
    path('post/create', views.CreatePost.as_view(), name='create_post'),
    path('reply/<int:post_id>/<int:comment_id>', views.PostAddReply.as_view(), name='add_reply'),
]