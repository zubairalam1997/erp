# Generated by Django 3.0.3 on 2021-12-21 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customernew_vendornew'),
        ('finance', '0002_auto_20211221_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='client_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.CustomerNew'),
        ),
    ]