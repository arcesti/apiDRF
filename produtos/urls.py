from django.urls import path
from .views.produto_view import ProdutoView

urlpatterns = [
    path('produtos/', ProdutoView.as_view())
]