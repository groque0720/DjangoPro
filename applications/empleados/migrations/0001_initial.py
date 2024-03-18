# Generated by Django 5.0.2 on 2024-03-11 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0002_alter_departamento_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Otro')], max_length=1, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento')),
            ],
        ),
    ]