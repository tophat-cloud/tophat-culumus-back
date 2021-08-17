# Generated by Django 3.2.6 on 2021-08-17 10:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import nanoid.generate


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('password_hash', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(default=nanoid.generate, max_length=21, primary_key=True, serialize=False)),
                ('domain', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cumulus.member')),
            ],
        ),
        migrations.CreateModel(
            name='Thunder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thunder_name', models.CharField(max_length=255)),
                ('priority', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cumulus.project')),
            ],
        ),
        migrations.CreateModel(
            name='ThunderSupport',
            fields=[
                ('statusCode', models.IntegerField(primary_key=True, serialize=False)),
                ('suggestion', models.TextField()),
                ('rel_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ThunderSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insecureCode', models.TextField()),
                ('comment', models.TextField()),
                ('thunder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cumulus.thunder')),
                ('thunder_support_statusCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cumulus.thundersupport')),
            ],
        ),
    ]
