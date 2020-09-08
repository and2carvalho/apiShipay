from django.urls import path, include
from rest_framework import routers
from .views import PagamentoView, pesquisaCliente

app_name = 'api'

router = routers.DefaultRouter()
router.register('v1/transacao', PagamentoView)

urlpatterns = [
    path('', include(router.urls), name='transacao'),
    path('pesquisaCliente/', pesquisaCliente, name='pesquisa-cliente')
]
