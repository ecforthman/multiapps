# Generated by Django 2.2 on 2021-04-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('date_submitted', models.DateTimeField(verbose_name='document date')),
                ('encrypted_text', models.TextField()),
                ('notes', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
