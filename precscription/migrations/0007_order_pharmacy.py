# Generated by Django 3.1.7 on 2021-03-07 15:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('precscription', '0006_auto_20210307_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='pharmacy')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='address')),
                ('postal_code', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message="Please use this format: 'XXXXX'.", regex='^\\d{5}$')])),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='city')),
                ('country', models.CharField(blank=True, max_length=30, verbose_name='country')),
                ('drug', models.ManyToManyField(to='precscription.Drug')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('ordered', models.BooleanField(default=False)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy', to='precscription.pharmacy')),
                ('precscriptions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_precscriptions', to='precscription.precscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
