# Generated by Django 2.2.27 on 2022-04-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220403_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before', models.CharField(max_length=200, verbose_name='日本語')),
                ('after', models.CharField(max_length=200, verbose_name='訳語')),
            ],
        ),
        migrations.DeleteModel(
            name='Words',
        ),
    ]
