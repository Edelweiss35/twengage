# Generated by Django 2.1.1 on 2018-09-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Name')),
                ('email', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Email')),
                ('message', models.CharField(blank=True, default=None, max_length=2000, null=True, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_username', models.CharField(blank=True, default=None, max_length=200, verbose_name='Twitter Username')),
                ('twitter_password', models.CharField(blank=True, default=None, max_length=200, verbose_name='Twitter Password')),
                ('package_id', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Package Id')),
                ('order_active', models.BooleanField(default=False, verbose_name='Order Active')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated At')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
            ],
        ),
    ]
