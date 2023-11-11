from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_create_view),
    # path('', views.product_all_views), # functional view from scratch
    # path('<int:id>/', views.product_all_views), # functional view from scratch
    path('<int:id>/', views.ProductDetailApiView.as_view(), name="product-detail"),
    path('<int:id>/update/', views.ProductUpdateApiView.as_view(), name="product-edit"),
    path('<int:id>/delete/', views.ProductDestroyApiView.as_view()),
    path('mixins/', views.ProductMixinView.as_view()),
    path('mixins/<int:id>/', views.ProductMixinView.as_view()),
]