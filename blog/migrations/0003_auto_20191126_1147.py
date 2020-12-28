# Generated by Django 2.1 on 2019-11-25 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191126_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
        ),
        migrations.AlterField(
            model_name='wateroff',
            name='city',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Cities', verbose_name='Населенный пункт'),
        ),
    ]
