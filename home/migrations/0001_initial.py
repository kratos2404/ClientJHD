# Generated by Django 4.1.5 on 2023-01-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='design')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VastuMaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog')),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('dimension', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('plot_area', models.CharField(max_length=100)),
                ('floors', models.CharField(max_length=50)),
            ],
        ),
    ]
