from django.urls import path
from productos import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('api/producto/',views.ProductoView.as_view(),name='producto'),
    path('api/producto/<int:p_id>',views.ProductoDetailView.as_view())
]