# Generated by Django 2.2.3 on 2019-07-18 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='recruit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='recruit_app.Form_Response'),
        ),
    ]
