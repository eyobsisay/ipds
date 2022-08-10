# Generated by Django 4.0.6 on 2022-08-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_Appriasal', '0004_rename_project_finance_source_projectappraisalmedia_quarter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectappraisalmedia',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='projectappraisalmedia',
            name='video_file',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
