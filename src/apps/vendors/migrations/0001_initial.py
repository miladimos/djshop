# Generated by Django 4.1 on 2023-09-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('logo', models.ImageField(upload_to='')),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('province', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('telegram', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'فروشنده',
                'verbose_name_plural': 'فروشنده ها',
                'db_table': 'vendors',
            },
        ),
    ]
