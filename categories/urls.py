from django.urls import path
from . import views


urlpatterns = [
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('subcategory/list/', views.SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/create/', views.SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/detail/', views.SubCategoryDetailView.as_view(), name='subcategory_detail'),
    path('subcategory/<int:pk>/update/', views.SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', views.SubCategoryDeleteView.as_view(), name='subcategory_delete'),
    path('subcategory/<int:category_id>/', views.load_subcategories, name='load_subcategories')
]
