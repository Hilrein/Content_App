from django.urls import path
from .views import (
    content_list, content_detail, content_create, content_update, content_delete,
    create_category, category_list, calendar_view
)

urlpatterns = [
    # Контент
    path('', content_list, name='content_list'),
    path('content/<int:content_id>/', content_detail, name='content_detail'),
    path('content/create/', content_create, name='content_create'),
    path('content/<int:content_id>/update/', content_update, name='content_update'),
    path('content/<int:content_id>/delete/', content_delete, name='content_delete'),

    # Категории
    path("categories/create/", create_category, name="create_category"),
    path('categories/', category_list, name='category_list'),


    # Календарь
    path('calendar/', calendar_view, name='calendar_view'),
    path('calendar/<int:year>/<int:month>/', calendar_view, name='calendar_view_month'),
]
