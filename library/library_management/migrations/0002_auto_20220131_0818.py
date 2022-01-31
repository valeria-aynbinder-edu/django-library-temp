# Generated by Django 3.2.11 on 2022-01-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]