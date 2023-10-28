from django.urls import path

from . import views


urlpatterns = [
    path('', views.MainCategoryList.as_view(), name='category_list'),
    path('product/', views.ProductListView.as_view(), name='ProductListView'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('category/<str:cats>/', views.category_view, name='product_category'),
    path('search_product/', views.search_product, name='search_product'),
    path('productcategory/', views.ProductCategoryView.as_view(), name='product_category'),
]
