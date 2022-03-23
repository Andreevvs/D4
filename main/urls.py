from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, PostCreateView,PostUpdateView, PostDeleteView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search/', NewsSearch.as_view()),
    path('add/', PostCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='news_delete'),
    ]