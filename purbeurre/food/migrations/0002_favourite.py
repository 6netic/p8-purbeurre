# Generated by Django 3.1 on 2020-09-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('former_barcode', models.CharField(max_length=80)),
                ('favourite_barcode', models.CharField(max_length=80)),
                ('email_user', models.EmailField(max_length=150)),
            ],
            options={
                'db_table': 'favourite',
                'managed': True,
            },
        ),
    ]