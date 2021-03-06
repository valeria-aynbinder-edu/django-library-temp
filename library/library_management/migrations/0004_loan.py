# Generated by Django 3.2.11 on 2022-01-31 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='library_management.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='library_management.customer')),
            ],
        ),
    ]
