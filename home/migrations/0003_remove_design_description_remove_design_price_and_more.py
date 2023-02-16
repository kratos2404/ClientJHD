# Generated by Django 4.1.5 on 2023-02-07 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_content_contact_map_requirements_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='description',
        ),
        migrations.RemoveField(
            model_name='design',
            name='price',
        ),
        migrations.RemoveField(
            model_name='vastumaps',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vastumaps',
            name='description',
        ),
        migrations.RemoveField(
            model_name='vastumaps',
            name='dimension',
        ),
        migrations.RemoveField(
            model_name='vastumaps',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='vastumaps',
            name='floors',
        ),
        migrations.RemoveField(
            model_name='vastumaps',
            name='plot_area',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='plot_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]