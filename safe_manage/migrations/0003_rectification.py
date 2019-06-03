# Generated by Django 2.2.1 on 2019-05-28 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safe_manage', '0002_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rectification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safe_manage.Problem')),
            ],
        ),
    ]
