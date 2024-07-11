from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home, name='home'),
	path('', views.product_list, name='product_list'),
	path('<int:pk>/', views.product_detail, name='product_detail'),
	path('<int:pk>/edit/', views.edit_product, name='edit_product'),
	path('<int:pk>/delete/', views.delete_product, name='delete_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
