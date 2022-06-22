# Generated by Django 4.0.5 on 2022-06-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('seller', 'Seller'), ('buyer', 'Buyer')], max_length=10),
        ),
    ]