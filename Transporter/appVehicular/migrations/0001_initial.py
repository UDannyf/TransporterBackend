# Generated by Django 2.2.7 on 2020-08-25 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('idCompany', models.AutoField(primary_key=True, serialize=False)),
                ('nameCompany', models.CharField(blank=True, max_length=45, null=True)),
                ('typeCompany', models.CharField(blank=True, max_length=45, null=True)),
                ('addressCompany', models.CharField(blank=True, max_length=45, null=True)),
                ('webpageCompany', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
    ]