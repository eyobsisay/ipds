# Generated by Django 4.0.6 on 2022-08-09 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_Appriasal', '0002_projectappraisal_project_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abroad',
            name='name',
            field=models.CharField(choices=[('Loan', 'Loan'), ('Grant Aid', 'Grant Aid')], max_length=50),
        ),
        migrations.CreateModel(
            name='ProjectAppraisalMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.ImageField(null=True, upload_to='project_appraisal_image')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('project_finance_source', models.CharField(choices=[('First', 'First'), ('second', 'Second'), ('Third', 'Third'), ('Forth', 'Forth')], max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_Appriasal.projectappraisal')),
            ],
        ),
    ]
