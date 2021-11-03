# Generated by Django 3.2.4 on 2021-11-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0084_auto_20211024_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudes',
            name='plan',
        ),
        migrations.AddField(
            model_name='quotes',
            name='finca',
            field=models.CharField(help_text='Número de folio real', max_length=100, null=True, verbose_name='Número de Finca'),
        ),
        migrations.AddField(
            model_name='quotes',
            name='internal_review',
            field=models.DateField(blank=True, help_text='Colocar Fecha dd/mm/año', null=True, verbose_name='Revisión interna:'),
        ),
        migrations.AddField(
            model_name='quotes',
            name='plan',
            field=models.URLField(blank=True, help_text='Link del plano, por favor', verbose_name='Plano'),
        ),
        migrations.AddField(
            model_name='quotes',
            name='preliminary_date',
            field=models.DateField(blank=True, help_text='Colocar Fecha dd/mm/año', null=True, verbose_name='Fecha preliminar:'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Área del proyecto'),
        ),
    ]