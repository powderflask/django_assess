# Generated by Django 2.2.7 on 2019-11-18 06:38

import assessment.builder.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('active', 'Active'), ('retired', 'Retired')], default='active', max_length=8)),
                ('label', models.CharField(help_text='Unique label for this classification. e.g., Education & Research', max_length=64)),
                ('slug', models.SlugField(help_text='Unique, short abbreviation e.g., edu-research for Education & Research', max_length=64, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description of the classification.')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': '1. Activities',
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssessmentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('active', 'Active'), ('retired', 'Retired')], default='active', max_length=8)),
                ('label', models.CharField(blank=True, help_text='Unique label for this assessment. e.g., Student Learning Experience', max_length=64)),
                ('slug', models.SlugField(blank=True, help_text='Unique, short abbreviation for category. e.g. student-experience', max_length=64, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description of this Assessment Category.')),
            ],
            options={
                'verbose_name': 'Assessment Category',
                'verbose_name_plural': '3. Assessment Categories',
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('active', 'Active'), ('retired', 'Retired')], default='active', max_length=8)),
                ('label', models.CharField(help_text='Label for this metric. e.g., Uses appropriate font size', max_length=64)),
                ('description', models.TextField(blank=True, help_text='Optional description of how to assess this metric.')),
            ],
            options={
                'verbose_name': 'Metric',
                'verbose_name_plural': '5. Metrics',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='AssessmentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('active', 'Active'), ('retired', 'Retired')], default='active', max_length=8)),
                ('label', models.CharField(help_text='Short label for this question. e.g., Use of Visual Aids', max_length=64)),
                ('description', models.TextField(blank=True, help_text='Complete question text or detailed description of concern to be assessed.')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': '4. Questions',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='MetricChoicesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='Short label for these choices. e.g., Percentage Range', max_length=64)),
                ('choice_map', models.TextField(help_text='JSON enoded dictionary mapping choices to integer values. \n                                               E.g., { "< 80%" : 0, "80 - 90%" : 1, ">90%" : 2 }', validators=[assessment.builder.validators.validate_JSON_scoring_choices], verbose_name='Choices')),
            ],
            options={
                'verbose_name': 'Metric Choices Type',
                'verbose_name_plural': 'Metric Choices Types',
            },
        ),
        migrations.CreateModel(
            name='ReferenceDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('label', models.CharField(help_text='Short label for this document. e.g., SOP Classroom Safety', max_length=128)),
                ('description', models.TextField(blank=True, help_text='Optional description of document and/or how it is used in the Assessment.')),
                ('url', models.URLField(help_text='URL for this document. e.g., https://docs.example.com/sop/classroom-safety.pdf ', max_length=256)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('active', 'Active'), ('retired', 'Retired')], default='active', max_length=8)),
                ('label', models.CharField(help_text='Unique label for this classification. e.g., Education & Research', max_length=64)),
                ('slug', models.SlugField(help_text='Unique, short abbreviation e.g., edu-research for Education & Research', max_length=64, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description of the classification.')),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': '2. Topics',
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='topic',
            constraint=models.UniqueConstraint(condition=models.Q(status='active'), fields=('label',), name='topic_unique_active_label'),
        ),
        migrations.AddField(
            model_name='referencedocument',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reference_docs', to='builder.AssessmentCategory'),
        ),
        migrations.AddField(
            model_name='assessmentquestion',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_set', to='builder.AssessmentCategory'),
        ),
        migrations.AddField(
            model_name='assessmentmetric',
            name='choices',
            field=models.ForeignKey(help_text='Define choices used to score this metric.', on_delete=django.db.models.deletion.CASCADE, to='builder.MetricChoicesType'),
        ),
        migrations.AddField(
            model_name='assessmentmetric',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metric_set', to='builder.AssessmentQuestion'),
        ),
        migrations.AddField(
            model_name='assessmentcategory',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_set', to='builder.Activity'),
        ),
        migrations.AddField(
            model_name='assessmentcategory',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_set', to='builder.Topic'),
        ),
        migrations.AddConstraint(
            model_name='activity',
            constraint=models.UniqueConstraint(condition=models.Q(status='active'), fields=('label',), name='activity_unique_active_label'),
        ),
        migrations.AddConstraint(
            model_name='assessmentcategory',
            constraint=models.UniqueConstraint(fields=('activity', 'topic'), name='unique_activity_topic'),
        ),
    ]
