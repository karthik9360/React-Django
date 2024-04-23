# Generated by Django 5.0.4 on 2024-04-23 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reactapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='React',
        ),
    ]
