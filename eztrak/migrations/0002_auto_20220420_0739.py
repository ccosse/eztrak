# Generated by Django 3.2.13 on 2022-04-20 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eztrak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='SiteStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='clients',
            field=models.ManyToManyField(related_name='projects', through='eztrak.ProjectClient', to='eztrak.Client'),
        ),
        migrations.AlterField(
            model_name='project',
            name='salesrep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rep', to='eztrak.employee'),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation Date')),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('red_grade', models.CharField(blank=True, choices=[('A', 'A Excellent'), ('B', 'B Better'), ('C', 'C Good'), ('D', 'D Fair'), ('E', 'E Lacking')], default='E', max_length=1, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('seen_from_street', models.BooleanField(default=False, null=True)),
                ('facing_street', models.BooleanField(default=False, null=True)),
                ('vacancies', models.BooleanField(default=False, null=True)),
                ('pylon_available', models.BooleanField(default=False, null=True)),
                ('center_type', models.CharField(blank=True, max_length=100, null=True)),
                ('traffic_a', models.CharField(blank=True, max_length=100, null=True)),
                ('traffic_a_num', models.IntegerField(blank=True, null=True)),
                ('traffic_b', models.CharField(blank=True, max_length=100, null=True)),
                ('traffic_b_num', models.IntegerField(blank=True, null=True)),
                ('anchor', models.CharField(blank=True, max_length=100, null=True)),
                ('distance_from_client', models.FloatField(blank=True, null=True)),
                ('anchor_walking_distance', models.CharField(blank=True, max_length=100, null=True)),
                ('escape_days', models.IntegerField(blank=True, null=True)),
                ('average_income', models.IntegerField(blank=True, null=True)),
                ('gross_income_projection', models.IntegerField(blank=True, null=True)),
                ('population_1m', models.IntegerField(blank=True, null=True)),
                ('population_3m', models.IntegerField(blank=True, null=True)),
                ('population_5m', models.IntegerField(blank=True, null=True)),
                ('avg_hh_income_1m', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('zip_code', models.CharField(max_length=10)),
                ('sl_comment', models.TextField(blank=True, null=True)),
                ('tenant_improvements', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('target_rent', models.FloatField(blank=True, null=True)),
                ('mark_read', models.BooleanField(default=False, null=True)),
                ('sqft', models.IntegerField(blank=True, null=True)),
                ('rba', models.IntegerField(blank=True, null=True)),
                ('rent_sf_yr', models.CharField(blank=True, default='0', max_length=32, null=True)),
                ('total_sf_available', models.IntegerField(blank=True, null=True)),
                ('r_comp', models.IntegerField(blank=True, null=True)),
                ('broker_company', models.CharField(blank=True, default='0', max_length=64, null=True)),
                ('broker_contact', models.CharField(blank=True, default='0', max_length=32, null=True)),
                ('broker_phone', models.CharField(blank=True, default='0', max_length=32, null=True)),
                ('broker_cell', models.CharField(blank=True, default='0', max_length=32, null=True)),
                ('broker_email', models.CharField(blank=True, default='email', max_length=64, null=True)),
                ('broker_address', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('broker_city', models.CharField(default='', max_length=32, null=True)),
                ('broker_state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='', max_length=2)),
                ('broker_zipcode', models.CharField(default='', max_length=10, null=True)),
                ('rawsite_note', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('director_note', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('lease_negotiator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CSM', to='eztrak.employee', verbose_name='Lease Negotiator')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eztrak.project', verbose_name='Project')),
                ('site_locator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SL', to='eztrak.employee', verbose_name='Site Locator')),
                ('site_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sc_status', to='eztrak.sitestatus', verbose_name='sctatus')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='eztrak.projectstatus'),
        ),
    ]
