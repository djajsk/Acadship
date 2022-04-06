# Generated by Django 4.0 on 2022-03-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_app_levels'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='salaries',
            field=models.CharField(blank=True, choices=[('Below 50,000', 'BELOW_50000'), ('50,000 - 100,000', '50000_100000'), ('100,000 - 200,000', '100000_200000'), ('Above 200,000', 'ABOVE_200000')], max_length=200, null=True, verbose_name='Salary Range'),
        ),
    ]
