# Generated by Django 3.1.7 on 2021-03-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precscription', '0008_auto_20210307_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drug',
            options={'verbose_name': 'drug', 'verbose_name_plural': 'drugs'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='pharmacy',
            options={'verbose_name': 'pharmacy', 'verbose_name_plural': 'pharmacies'},
        ),
        migrations.AlterModelOptions(
            name='precscription',
            options={'verbose_name': 'precscription', 'verbose_name_plural': 'pecscriptions'},
        ),
        migrations.AlterField(
            model_name='drug',
            name='strength_unit',
            field=models.CharField(choices=[('M', 'mg'), ('G', 'gm'), ('N', 'ng'), ('MC', 'mcg')], default='mg', max_length=3, verbose_name='strength unit'),
        ),
    ]
