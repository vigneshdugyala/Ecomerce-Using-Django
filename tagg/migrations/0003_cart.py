# Generated by Django 3.0.5 on 2020-05-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagg', '0002_auto_20200521_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.IntegerField()),
                ('products', models.IntegerField()),
            ],
        ),
    ]