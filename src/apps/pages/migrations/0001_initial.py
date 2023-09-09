# Generated by Django 4.1 on 2023-09-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='b0a441ba-b093-478c-8df4-532fde6dc712', unique=True)),
                ('is_deleted', models.BooleanField(blank=True, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('mobile', models.CharField(blank=True, max_length=12, null=True, verbose_name='موبایل')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name='ایمیل')),
                ('message', models.TextField(verbose_name='پیام')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='b0a441ba-b093-478c-8df4-532fde6dc712', unique=True)),
                ('is_deleted', models.BooleanField(blank=True, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='b0a441ba-b093-478c-8df4-532fde6dc712', unique=True)),
                ('is_deleted', models.BooleanField(blank=True, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('question', models.CharField(max_length=255, unique=True)),
                ('answer', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FaqGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='b0a441ba-b093-478c-8df4-532fde6dc712', unique=True)),
                ('is_deleted', models.BooleanField(blank=True, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]