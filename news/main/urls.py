from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('single/<int:news_id>', views.single, name='single'),
    path('comments/<int:news_id>/', views.comments, name='comments'),
    path('categories/<str:cat_id>/', views.category_detail, name='category_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
