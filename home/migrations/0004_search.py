# Generated by Django 4.1.5 on 2023-02-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_design_description_remove_design_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
