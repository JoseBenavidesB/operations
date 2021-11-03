# Generated by Django 3.2.4 on 2021-10-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0037_auto_20211005_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('finalizado', 'Finalizado'), ('sin_concluir', 'Sin concluir')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='amount_bill1',
            field=models.DecimalField(decimal_places=2, help_text='Digite el monto (máximo 2 decimales)', max_digits=9, verbose_name='Monto en $'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='amount_bill2',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Digite el monto (máximo 2 decimales)s', max_digits=9, null=True, verbose_name='Monto en $'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Digite el monto (máximo 2 decimales)', max_digits=9, null=True, verbose_name='Monto en $'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='amount2',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Digite el monto (máximo 2 decimales)', max_digits=9, null=True, verbose_name='Monto en ¢'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='status',
            field=models.CharField(choices=[('Pendiente Revisión', 'Pendiente Revisión'), ('Enviado al Cliente', 'Enviado al Cliente'), ('Pendiente de Envio', 'Pendiente de Envio'), ('Rechazado', 'Rechazado'), ('Aprobada', 'Aprobada')], max_length=50, null=True, verbose_name='Estatus'),
        ),
    ]