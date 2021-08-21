# Generated by Django 3.2.5 on 2021-08-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
    ]
