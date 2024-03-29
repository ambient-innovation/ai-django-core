# Generated by Django 3.2.8 on 2022-05-19 15:28

from django.db import migrations, models

import ai_django_core.mixins.validation


class Migration(migrations.Migration):
    dependencies = [
        ('testapp', '0005_modelwithcleanmixin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithSelector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
            ],
            bases=(ai_django_core.mixins.validation.CleanOnSaveMixin, models.Model),
        ),
    ]
