# Generated by Django 3.2.2 on 2021-05-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
