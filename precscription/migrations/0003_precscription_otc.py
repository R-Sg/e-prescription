# Generated by Django 3.1.7 on 2021-03-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precscription', '0002_auto_20210307_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='precscription',
            name='otc',
            field=models.CharField(default='covid', max_length=100, verbose_name='over the counter medicine'),
            preserve_default=False,
        ),
    ]
