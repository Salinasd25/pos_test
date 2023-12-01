from django.db import models

class Product(models.Model):
    barcode = models.CharField(
        max_length=255, 
        unique=True, 
        verbose_name='Codigo de Barras'
    )
    name = models.CharField(
        max_length=255,
        help_text='Nombre',
    )
    descripcion = models.TextField(
        blank=True, 
        null=True, 
        help_text='Descripcion del producto'
    )
    price = models.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        help_text='Precio del producto'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        help_text='Fecha de creación del objeto'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text='Fecha de creación del objeto'
    )
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'product'
        ordering = ('-id',)