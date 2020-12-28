# Generated by Django 2.1 on 2019-10-15 02:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.SlugField(blank=True, max_length=150, unique=True)),
                ('body', ckeditor.fields.RichTextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]