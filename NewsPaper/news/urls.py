from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (
    PostList, PostDetail, PostCreate,
    PostUpdate, PostDelete, ArticleCreate,
    ArticleUpdate, ArticleDelete, subscriptions
)

urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),

    path('news/create/', cache_page(60*10)(PostCreate.as_view()), name='post_create'),
    path('news/<int:pk>/update/', cache_page(60*5)(PostUpdate.as_view()), name='post_update'),
    path('news/<int:pk>/delete/', cache_page(60*5)(PostDelete.as_view()), name='post_delete'),

    path('article/create/', cache_page(60*5)(ArticleCreate.as_view()), name='article_create'),
    path('article/<int:pk>/update/', cache_page(60*5)(ArticleUpdate.as_view()), name='article_update'),
    path('article/<int:pk>/delete/', cache_page(60*5)(ArticleDelete.as_view()), name='article_delete'),

    path('subscriptions/', subscriptions, name='subscriptions'),

]
