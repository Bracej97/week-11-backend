# Generated by Django 4.2.16 on 2024-12-02 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issueTrackerBackendApp', '0004_alter_issue_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 2, 18, 47, 29, 356711, tzinfo=datetime.timezone.utc)),
        ),
    ]
