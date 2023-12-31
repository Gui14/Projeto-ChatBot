# Generated by Django 3.2.22 on 2023-10-17 18:11

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info_cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('senha', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=300)),
                ('bairro', models.CharField(max_length=50)),
                ('telefone', models.IntegerField(max_length=15)),
                ('nome_guardiao', models.CharField(max_length=200)),
                ('email_guardiao', models.EmailField(blank=True, max_length=254)),
                ('telefone_guardiao', models.IntegerField(max_length=15)),
            ],
        ),
    ]
