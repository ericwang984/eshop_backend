# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-01-19 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('slug', django_extensions.db.fields.ShortUUIDField(blank=True, editable=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user appears under Customer or Staff and can log into this admin site', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user is active and can log in', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('has_set_password', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'U', b'Unspecified')], default=b'U', max_length=1)),
                ('is_vip', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['email'],
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]