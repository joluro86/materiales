# Generated by Django 4.0.6 on 2022-08-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlmateriales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matfenix',
            name='concatenacion',
            field=models.CharField(default='0', max_length=100, verbose_name='Concat'),
        ),
        migrations.AddField(
            model_name='matperseo',
            name='concatenacion',
            field=models.CharField(default='0', max_length=100, verbose_name='Concat'),
        ),
    ]