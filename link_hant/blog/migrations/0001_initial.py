# Generated by Django 3.1.5 on 2021-02-21 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='#hashtag')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'db_table': 'tags',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Commentator email.')),
                ('comment', models.TextField(verbose_name='Content.')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Created.')),
                ('is_moderated', models.BooleanField(default=False, verbose_name='Is modetated.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='User.')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Record title.')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create date.')),
                ('text', models.TextField(verbose_name='Record content.')),
                ('tags', models.ManyToManyField(related_name='hashtags', to='blog.Tags', verbose_name='#hashtag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL, verbose_name='User.')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'db_table': 'blogs',
                'ordering': ('-create', '-id'),
            },
        ),
    ]
