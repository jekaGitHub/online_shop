# Generated by Django 4.2.2 on 2024-03-24 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='a305cd3bf8ddcf946ba2ad671280170d', max_length=50, verbose_name='Токен'),
            preserve_default=False,
        ),
    ]