from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Pagamento
from .serializer import PagamentoSerializer


class PagamentoView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
                        'aceito': True
                    })

@api_view(['POST'])
def pesquisaCliente(request):
    if request.method == 'POST':
        if request.data.get('cliente'):
            try:
                cliente = request.data.get('cliente')
                query = Pagamento.objects.filter(cliente=cliente)
                return JsonResponse(PagamentoSerializer(query, many=True).data,safe=False)
            except Pagamento.DoesNotExist:
                return JsonResponse(
                    {'error':'Não existe pagamentos para o cliente informado'}
                )
    return JsonResponse(
        {'error': 'Informe um cliente para fazer a busca'})