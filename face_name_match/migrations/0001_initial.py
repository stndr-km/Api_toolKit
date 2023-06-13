# Generated by Django 3.1.2 on 2023-06-11 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facematching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_column='created_on', default=django.utils.timezone.localtime)),
                ('updated_on', models.DateTimeField(db_column='updated_on', default=django.utils.timezone.localtime)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.CharField(max_length=200, null=True)),
                ('match_percentage', models.FloatField(null=True)),
                ('image1', models.ImageField(upload_to='facematch/')),
                ('image2', models.ImageField(upload_to='facematch/')),
                ('message', models.CharField(max_length=200, null=True)),
            ],
            options={
                'ordering': ('-updated_on', '-created_on'),
                'get_latest_by': 'updated_on',
                'abstract': False,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='StringMatching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_column='created_on', default=django.utils.timezone.localtime)),
                ('updated_on', models.DateTimeField(db_column='updated_on', default=django.utils.timezone.localtime)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name1', models.CharField(max_length=200, null=True)),
                ('name2', models.CharField(max_length=200, null=True)),
                ('match_percentage', models.FloatField(null=True)),
            ],
            options={
                'ordering': ('-updated_on', '-created_on'),
                'get_latest_by': 'updated_on',
                'abstract': False,
                'default_permissions': (),
            },
        ),
    ]
