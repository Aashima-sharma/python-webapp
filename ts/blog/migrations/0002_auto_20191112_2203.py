# Generated by Django 2.2.6 on 2019-11-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('chead0', models.CharField(default='', max_length=5000)),
                ('head1', models.CharField(default='', max_length=500)),
                ('chead1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=500)),
                ('chead2', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_id', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=500)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
