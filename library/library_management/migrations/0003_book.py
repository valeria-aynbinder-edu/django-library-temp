# Generated by Django 3.2.11 on 2022-01-31 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0002_auto_20220131_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('year_published', models.IntegerField()),
                ('genre', models.CharField(blank=True, choices=[('scifi', 'Sci-Fi'), ('history', 'History'), ('classics', 'Classics'), ('horror', 'Horror'), ('kids', 'Kids')], max_length=128, null=True)),
                ('book_type', models.PositiveSmallIntegerField(default=1)),
                ('copies_num', models.PositiveSmallIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='library_management.author')),
            ],
        ),
    ]
