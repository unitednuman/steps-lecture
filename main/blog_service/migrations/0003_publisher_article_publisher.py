# Generated by Django 4.2.1 on 2023-06-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_service', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='publisher',
            field=models.ManyToManyField(to='blog_service.publisher'),
        ),
    ]