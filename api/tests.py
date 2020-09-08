from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Pagamento
from api.serializer import PagamentoSerializer

class TransacaoTeste(APITestCase): 
 
    def test_create(self): 
        url = '/api/v1/transacao/'
        data = {
            "estabelecimento": "45.283.163/0001-67",
            "cliente": "094.214.930-01",
            "valor": 590.01,
            "descricao": "Almoço em restaurante chique pago via Shipay!"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pagamento.objects.count(),1) 
        self.assertEqual(Pagamento.objects.get().cliente,"094.214.930-01")