# Generated by Django 3.1.6 on 2021-04-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRApp', '0007_auto_20210401_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
