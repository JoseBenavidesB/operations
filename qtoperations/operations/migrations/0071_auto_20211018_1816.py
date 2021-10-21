# Generated by Django 3.2.4 on 2021-10-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0070_auto_20211017_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('sin_concluir', 'Sin concluir'), ('finalizado', 'Finalizado')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='sub_customers',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
    ]
