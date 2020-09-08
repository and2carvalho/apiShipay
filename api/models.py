from django.db import models

class Pagamento(models.Model):

    estabelecimento = models.CharField('Estabelecimento', max_length=60, blank=False)
    cliente = models.CharField('Cliente', max_length=14,blank=False)
    valor = models.DecimalField('Valor', max_digits=9, decimal_places=2, blank=False)
    descricao = models.TextField('Descrição', blank=False)

    def __str__(self):
        return self.descricao

