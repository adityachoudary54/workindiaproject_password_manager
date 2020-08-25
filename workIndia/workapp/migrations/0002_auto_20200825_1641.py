# Generated by Django 3.1 on 2020-08-25 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='PasswordManager',
        ),
        migrations.AddField(
            model_name='passwords',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workapp.user'),
        ),
    ]