# Generated by Django 4.0.4 on 2022-05-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('specialization', models.TextField()),
                ('ob_id', models.TextField()),
                ('department_id', models.TextField()),
                ('work_period', models.TextField()),
            ],
        ),
    ]
