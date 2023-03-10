# Generated by Django 4.1.7 on 2023-02-21 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(help_text='Required, Id of product', on_delete=django.db.models.deletion.PROTECT, to='supermarket.product')),
            ],
            options={
                'db_table': 'supermarket_product_request_log',
            },
        ),
    ]
