# Generated by Django 5.2.1 on 2025-05-18 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0001_initial'),
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colaboradores', to='grupos.grupo'),
        ),
    ]
