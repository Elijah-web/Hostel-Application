# Generated by Django 3.0.3 on 2020-03-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0012_auto_20200323_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel',
            name='hostel_unique_identifier',
        ),
        migrations.AddField(
            model_name='hostel',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]