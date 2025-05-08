from rest_framework.views import APIView
from rest_framework.response import Response
from produtos.models import Produto
from produtos.serializers.produto_serializer import ProdutoSerializer

class ProdutoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                produto = Produto.objects.get(id=pk)
                serializer = ProdutoSerializer(produto)
                return Response(serializer.data)
            except Produto.DoesNotExist:
                return Response({"detail":"Produto não encontrado!"}, 400)
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        if not pk:
            return Response({"detail": "Objeto não existe"}, 400)
        try:
            produto = Produto.objects.get(id=pk)
        except Produto.DoesNotExist:
            return Response({ "erro": "Produto não encontrado."}, status=400)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "message": "Objeto atualizado com sucesso", "Objeto atualizado": serializer.data })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if not pk:
            return Response({ "message": "Não há nenhum id no parametro" }, status=400)
        try:
            produto = Produto.objects.get(id=pk)
            produto_data = ProdutoSerializer(produto).data
            produto.delete()
            return Response({ "message": "Objeto excluido com sucesso!", "Objeto": produto_data })
        except Produto.DoesNotExist:
            return Response({ "message": "Objeto não encontrado!" }, status=404)
        