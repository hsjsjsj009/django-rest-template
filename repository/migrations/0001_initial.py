# Generated by Django 3.1.7 on 2021-03-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer_field', models.IntegerField()),
                ('text_field', models.TextField()),
            ],
        ),
    ]