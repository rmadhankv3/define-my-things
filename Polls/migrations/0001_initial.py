# Generated by Django 2.0.7 on 2018-09-12 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('char_limit', models.IntegerField()),
                ('mandatory', models.BooleanField(default=False)),
                ('multi_line_text', models.BooleanField(default=False)),
                ('question_text', models.TextField()),
                ('question_type', models.CharField(choices=[('Text', 'Text'), ('Checkbox', 'Checkbox'), ('Radio button', 'Radio button')], default='Text', max_length=15)),
                ('sequence', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Poll_Question_Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('answer_Option', models.TextField()),
                ('sequence', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Poll_Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.Poll_Question')),
            ],
        ),
        migrations.CreateModel(
            name='Poll_Response_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('question_text', models.TextField()),
                ('answer_given', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Poll_Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.Poll_Question')),
            ],
        ),
        migrations.CreateModel(
            name='Poll_Response_Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_on', models.DateTimeField(blank=True, null=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Poll_Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('chart_title', models.CharField(max_length=30)),
                ('country', models.TextField()),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('url', models.URLField()),
                ('status', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='poll_response_sheet',
            name='Poll_Template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.Poll_Template'),
        ),
        migrations.AddField(
            model_name='poll_response_sheet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poll_response_answer',
            name='Poll_Response_Sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.Poll_Response_Sheet'),
        ),
        migrations.AddField(
            model_name='poll_response_answer',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poll_question',
            name='Poll_Template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.Poll_Template'),
        ),
    ]
