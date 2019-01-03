# Generated by Django 2.1 on 2019-01-03 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SchoolStudents', '0003_userprofile_user_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_one', models.CharField(max_length=300)),
                ('option_two', models.CharField(blank=True, max_length=300, null=True)),
                ('answers_marks', models.IntegerField(default=0)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('Multiple Choice Question ', 'MCQ'), ('True/False', 'TRUEFALSE'), ('Fill in the blanks', 'FILLINBLANKS'), ('Match the Following', 'MATCHTHEFOLLOWING'), ('Comprehension', 'COMPREHENSION')], max_length=10, unique=True)),
                ('question_title', models.TextField()),
                ('question_marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuestionBank.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionBank.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionBanks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(default=100, null=True)),
                ('total_time', models.DateTimeField(blank=True)),
                ('general_instructions', models.TextField(blank=True, null=True)),
                ('ques_bank_title', models.CharField(blank=True, max_length=200)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('exam_start_time', models.TimeField(auto_now_add=True)),
                ('exam_end_time', models.TimeField(auto_now_add=True)),
                ('author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('ques_grades', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='SchoolStudents.Grades')),
                ('ques_sections', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='SchoolStudents.Sections')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsSections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(blank=True, max_length=200)),
                ('comprehension_desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentQuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuestionBank.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionBank.Question')),
            ],
        ),
        migrations.CreateModel(
            name='StudentResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_scored', models.IntegerField(blank=True, default=0)),
                ('is_present', models.BooleanField(default=False)),
                ('question_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionBank.QuestionBanks')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolStudents.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='questionbanks',
            name='student_assigned_list',
            field=models.ManyToManyField(through='QuestionBank.StudentResponse', to='SchoolStudents.UserProfile'),
        ),
        migrations.AddField(
            model_name='questionbanks',
            name='subject',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuestionBank.Subject'),
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuestionBank.QuestionsSections'),
        ),
    ]