# Generated by Django 4.0.6 on 2022-08-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlmateriales', '0006_matfenix_enperseo_matperseo_enfenix'),
    ]

    operations = [
        migrations.CreateModel(
            name='faltanteperseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concatenacion', models.CharField(default='0', max_length=100, verbose_name='Concat')),
                ('pedido', models.CharField(max_length=10, verbose_name='Pedido')),
                ('actividad', models.CharField(max_length=500, verbose_name='Actividad')),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Cantidad')),
                ('acta', models.CharField(default=0, max_length=100, verbose_name='Acta')),
            ],
            options={
                'verbose_name': 'Faltante Perseo',
                'verbose_name_plural': 'Faltante Perseo',
                'db_table': 'faltanteperseo',
                'ordering': ['fecha'],
            },
        ),
    ]