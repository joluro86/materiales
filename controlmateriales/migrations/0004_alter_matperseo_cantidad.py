# Generated by Django 4.0.6 on 2022-08-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlmateriales', '0003_matperseo_acta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matperseo',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Cantidad'),
        ),
    ]
