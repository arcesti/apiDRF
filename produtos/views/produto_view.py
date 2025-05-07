from rest_framework.views import APIView
from rest_framework.response import Response
from produtos.models import Produto
from produtos.serializers.produto_serializer import ProdutoSerializer

class ProdutoView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
