# Generated by Django 3.0.3 on 2021-12-18 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planId', models.CharField(max_length=30, null=True)),
                ('Type', models.CharField(choices=[('PREPAID', 'Prepaid'), ('POSTPAID', 'Postpaid')], max_length=20, null=True)),
                ('duration', models.CharField(max_length=20, null=True)),
                ('dateOfCreation', models.DateField(null=True)),
                ('validity', models.DateField(null=True)),
                ('billingCycle', models.DateField(null=True)),
                ('dueDate', models.DateField(null=True)),
                ('terms', models.TextField(max_length=250, null=True, verbose_name='PlanTerms')),
            ],
            options={
                'verbose_name_plural': 'plan',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_no', models.CharField(max_length=30, null=True)),
                ('Product_name', models.CharField(max_length=20, null=True)),
                ('cost', models.FloatField()),
                ('Company_name', models.CharField(max_length=20)),
                ('Product_Description', models.TextField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'product',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serviceId', models.CharField(max_length=50)),
                ('name_c', models.CharField(max_length=100, verbose_name='company')),
                ('Type', models.CharField(blank=True, default='Unknown', max_length=20, null=True, verbose_name='Type')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('rate', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('discount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('Tax', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Service',
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_no', models.CharField(blank=True, max_length=20, null=True)),
                ('complaint', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('stage', models.CharField(choices=[('initialize', 'INITIALIZE'), ('inprogress', 'INPROGRESS'), ('solved', 'SOLVED')], max_length=50)),
                ('status', models.CharField(choices=[('inprogress', 'INPROGRESS'), ('solved', 'SOLVED')], max_length=50)),
                ('solution', models.TextField(blank=True, max_length=500, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
                ('complaint_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.Customer')),
                ('complaint_handler', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('complaint_related_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.Service')),
            ],
        ),
    ]