# Generated by Django 4.2.6 on 2023-12-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Image', models.CharField(max_length=2083)),
            ],
        ),
    ]
