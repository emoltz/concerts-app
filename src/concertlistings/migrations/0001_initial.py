# Generated by Django 4.1 on 2022-08-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.CharField(max_length=240, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=240)),
                ('artist', models.CharField(max_length=240)),
                ('venue', models.CharField(max_length=240)),
                ('date', models.DateTimeField()),
                ('genre', models.CharField(max_length=240)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('ticket_url', models.TextField()),
            ],
        ),
    ]
