from django.conf.urls.static import static
from django.urls import path

from Fans_MMORPG import settings
from . import views
from .views import PostList, PostDetail, PostCreate, PostEdit, PostDelete, MessagesList, delete_message, mark_as_read, MyPostsList

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('messages/', MessagesList.as_view(), name='messages'),
    path('createpost/', PostCreate.as_view(), name ='create_post'),
    path('updatepost/<int:pk>', PostEdit.as_view(), name='edit_post'),
    path('deletepost/<int:pk>', PostDelete.as_view(), name='delete_post'),
    path('myposts/', MyPostsList.as_view(), name='my_posts'),

    path('deletemessage/<int:pk>', views.delete_message, name='delete_message'),
    path('markasread/<int:pk>', views.mark_as_read, name='mark_as_read'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
