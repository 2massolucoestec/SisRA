# Generated by Django 2.0.4 on 2018-05-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180502_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='total_horas',
            field=models.TimeField(blank=True, null=True, verbose_name='Total'),
        ),
    ]