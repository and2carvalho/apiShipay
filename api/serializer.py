from rest_framework import serializers
from .models import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pagamento
        fields = ['pk', 'estabelecimento', 'cliente', 'valor', 'descricao']

