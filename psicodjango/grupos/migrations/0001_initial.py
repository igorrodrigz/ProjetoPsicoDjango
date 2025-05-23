# Generated by Django 5.2.1 on 2025-05-18 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to='empresas.empresa')),
            ],
            options={
                'verbose_name_plural': 'Grupos',
                'unique_together': {('nome', 'empresa')},
            },
        ),
    ]
