# Generated by Django 3.1.6 on 2021-03-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRApp', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]