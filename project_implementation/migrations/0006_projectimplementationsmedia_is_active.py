# Generated by Django 4.0.6 on 2022-08-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_implementation', '0005_rename_project_finance_source_projectimplementationsmedia_quarter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimplementationsmedia',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
