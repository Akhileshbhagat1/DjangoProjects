# Generated by Django 2.2.10 on 2020-03-02 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('loc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Courss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.IntegerField()),
                ('cname', models.CharField(max_length=30)),
                ('cfee', models.IntegerField()),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='many.Student')),
            ],
        ),
    ]