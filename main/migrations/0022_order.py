# Generated by Django 3.1.7 on 2021-03-19 13:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=None)),
                ('street', models.CharField(blank=True, default='', max_length=50)),
                ('house', models.CharField(blank=True, default='', max_length=50)),
                ('region', models.CharField(blank=True, default='', max_length=50)),
                ('postal_code', models.CharField(blank=True, default='', max_length=10)),
                ('phone', models.CharField(blank=True, default='', max_length=13)),
                ('payment_choice', models.CharField(choices=[('Home delivery', 'Home delivery'), ('Take away', 'Take away')], default=1, max_length=30)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customers', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
