# Generated by Django 5.1 on 2025-01-02 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('os_data_storage', '0002_server_1_cpu_count_server_1_cpu_freq_current_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Server_1',
        ),
    ]