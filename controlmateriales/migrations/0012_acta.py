# Generated by Django 4.0.6 on 2022-08-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlmateriales', '0011_guia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Acta',
                'verbose_name_plural': 'Actas',
            },
        ),
    ]
