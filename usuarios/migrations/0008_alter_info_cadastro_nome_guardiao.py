# Generated by Django 3.2.22 on 2023-10-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20231017_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_cadastro',
            name='nome_guardiao',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
