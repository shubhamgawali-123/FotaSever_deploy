# Generated by Django 3.1.1 on 2020-10-19 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FotaUpdate', '0004_auto_20201018_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaigndetail',
            name='TargetVersion',
        ),
        migrations.RemoveField(
            model_name='campaigndetail',
            name='sourceVersion',
        ),
        migrations.RemoveField(
            model_name='campaigndetail',
            name='packageFile',
        ),
        migrations.AddField(
            model_name='campaigndetail',
            name='packageFile',
            field=models.ManyToManyField(to='FotaUpdate.ContentFile'),
        ),
        migrations.CreateModel(
            name='FwVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceVersion', models.CharField(max_length=100)),
                ('TargetVersion', models.CharField(max_length=100)),
                ('scomoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FotaUpdate.scomoid')),
            ],
        ),
    ]
