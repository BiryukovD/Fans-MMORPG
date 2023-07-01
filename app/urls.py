from django.conf.urls.static import static
from django.urls import path

from Fans_MMORPG import settings
from .views import PostList, PostDetail, PostCreate, PostEdit, PostDelete, MessagesList

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('messages/', MessagesList.as_view(), name='messages'),
    path('createpost/', PostCreate.as_view(), name ='create_post'),
    path('updatepost/<int:pk>', PostEdit.as_view(), name='edit_post'),
    path('deletepost/<int:pk>', PostDelete.as_view(), name='delete_post'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
