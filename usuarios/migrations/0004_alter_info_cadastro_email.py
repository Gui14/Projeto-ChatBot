# Generated by Django 3.2.22 on 2023-10-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_info_cadastro_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_cadastro',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
