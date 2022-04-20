if True:
	from django.core.validators import RegexValidator
	from django.contrib.auth.models import User
	from django.db import models
	import sys,logging

	FORMAT = '%(message)s'
	logging.basicConfig(filename='/var/log/testing.log',level=logging.INFO, format=FORMAT)

	state_choices=(
	('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'),
	('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'),
	('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'),
	('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'),
	('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'),
	('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'),
	('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
	('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
	('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
	('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'),
	('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'),
	('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
	('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'),
	('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
)
	color_theme_choices=(
	('indigo','indigo'),
	('blue','blue'),
	('black','black'),
	('dark-grey','dark-grey'),
	('grey','grey'),
	('brown','brown'),
	('blue-grey','blue-grey'),
	('deep-orange','deep-orange'),
	('orange','orange'),
	('amber','amber'),
	('yellow','yellow'),
	('khaki','khaki'),
	('lime','lime'),
	('light-green','light-green'),
	('green','green'),
	('teal','teal'),
	('cyan','cyan'),
	('light-blue','light-blue'),
	('deep-purple','deep-purple'),
	('purple','purple'),
	('pink','pink'),
	('red','red'),
	#('w3schools','w3schools'),
	('eztrak','eztrak')
);

class ProjectStatus(models.Model):
	title = models.CharField(max_length=100)
	#color = ColorField(default='#0000FF')
	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class SiteStatus(models.Model):
	title = models.CharField(max_length=100)
	#color = ColorField(default='#0000FF')
	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class ClientFinances(models.Model):
	fs_choices=(
		(1,"1 No cash, poor credit profile, no other resources.."),
		(2,"2 Maybe cash, no partner, limited credit call..."),
		(3,"3 Maybe cash, no additional resources, 100% financing..."),
		(4,"4 Part cash, part financing..."),
		(5,"5 Financing, some personal assets: i.e. 401k/IRS, current cc's, HELOC: NO CASH..."),
		(6,"6 Cash buyer..."),
		)
	amount_choices = (
		('0-50,000', '0-50,000'),
		('50,000-80-000', '50,000-80,000'),
		('80,000-120,000', '80,000-120,000'),
		('120,000-250,000', '120,000-250,000'),
		('Over 250,000', 'Over 250,000'),
	)
	date_of_birth = models.DateField('Date of Birth',null=True,blank=True)
	social_security = models.CharField("Social Security Number", max_length=32,null=True,blank=True)
	credit_score = models.IntegerField(default=0,null=True,blank=True)
	available_capital = models.CharField("Amount you plan to invest",max_length=30, null=True, blank=True,choices=amount_choices)#, verbose_name="Amount you plan to invest", choices=amount_choices)
	#
	place_of_employment = models.CharField('Place of Employment', null=True,blank=True,max_length=128)
	annual_salary = models.IntegerField('Annual Salary', null=True,blank=True)
	years_at_job = models.IntegerField('Years at Job', null=True,blank=True)
	#
	other_business = models.CharField(max_length=100, null=True, blank=True)
	open_in_one_to_three = models.BooleanField(null=True, blank=True)
	#
	working_capital = models.IntegerField("Working Capital", null=True, blank=True)
	#
	#NEED: Make these addable inline items w/type inc other; name=finance_vars
	financial_strength = models.IntegerField("Financial Strength",default=1,choices=fs_choices)
	financing_cash = models.DecimalField("Cash Funds", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_loc = models.DecimalField("Line of Credit", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_hloc = models.DecimalField("Home Equity LOC", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_401k = models.DecimalField("401K Funds", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_pension = models.DecimalField("Pension Funds", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_ira = models.DecimalField("IRA Funds", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_stocksbonds = models.DecimalField("Stocks and Bonds", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_cd = models.DecimalField("CD Funds", max_digits=10,  decimal_places=2, null=True, blank=True, default=0)
	financing_lifeinsurance = models.DecimalField("Life Insurance", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_credit = models.DecimalField("Credit Cards", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_financing_auto_loan = models.DecimalField("Auto Loan", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_mortgage_primary = models.DecimalField("Mortgage Primary", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_mortgage_other = models.DecimalField("Mortgage Other", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_installment = models.DecimalField("Installment Payments", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	financing_debts_other = models.DecimalField("Other Debts", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
	#
	fi_target_date = models.DateField('Finance Target Date', null=True, blank=True)
	fi_turnover_date = models.DateTimeField('Finance Turn Over Date', null=True, blank=True)
	#
	funding_path = models.CharField(max_length=100, null=True, blank=True)
	amount_preaproved = models.IntegerField("Amount Pre-Approved", null=True, blank=True)
	amount_obtained = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.finance.get().email

class Client(models.Model):
	email = models.EmailField("Email",null=True,blank=True,db_index=True)#builtin validator; client before user!
	password=models.CharField("Password",max_length=20,null=True,blank=True,default="")
	#
	last_name = models.CharField("Last name",max_length=60, null=True,blank=True, default="", db_index=True)
	first_name = models.CharField("First name",max_length=60, null=True,blank=True, default="")
	#
	finances = models.ForeignKey(ClientFinances,on_delete=models.SET_NULL,related_name='finance', null=True, blank=True)
	#
	google_name=models.CharField("Google name",max_length=60, null=True,blank=True, default="")
	google_id=models.CharField(max_length=30, null=True,blank=True, default="")
	google_img=models.URLField(null=True, blank=True)
	#
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone1 = models.CharField(validators=[phone_regex], max_length=30, blank=True, null=True) # validators should be a list
	phone2 = models.CharField(validators=[phone_regex], max_length=30, blank=True, null=True) # validators should be a list
	#
	address = models.CharField("Address",max_length=60, null=True, blank=True)
	city = models.CharField("City",max_length=30, null=True, blank=True)
	state = models.CharField("State",max_length=30, null=True, blank=True,choices=state_choices)
	zipcode = models.CharField("Zipcode",max_length=30, null=True, blank=True)
	country = models.CharField("Country",max_length=40, null=True, blank=True)
	#
	client_lat = models.FloatField(null=True, blank=True)
	client_lng = models.FloatField(null=True, blank=True)

class Employee(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='e_user')
	google_name=models.CharField("Google name",max_length=60, null=True,blank=True, default="")
	google_id=models.CharField(max_length=30, null=True,blank=True, default="")
	google_img=models.URLField(null=True, blank=True)
	color_theme = models.CharField(max_length=16,default='indigo',choices=color_theme_choices)

class Project(models.Model):
	project_status = models.ForeignKey(ProjectStatus,on_delete=models.CASCADE,related_name='status', null=True, blank=True)
	clients=models.ManyToManyField(Client,through="ProjectClient",related_name='projects')#actual qs of [Client]
	salesrep = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='rep', null=True, blank=True)
	store_city = models.CharField("City",max_length=30, null=True, blank=True)
	store_state = models.CharField("State",max_length=30, null=True, blank=True,choices=state_choices)
	store_zipcode = models.CharField("Zipcode",max_length=10, null=True, blank=True)
	store_lat = models.FloatField(null=True, blank=True)
	store_lng = models.FloatField(null=True, blank=True)

	def primary_client(self):
		for _pc in ProjectClient.objects.filter(project_id=self.id):
			if _pc.is_primary:
				return _pc.client
		return None

class ProjectClient(models.Model):
	project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='pcp', null=True, blank=True)
	client=models.ForeignKey(Client,on_delete=models.CASCADE,related_name='pcc', null=True, blank=True)
	is_primary=models.BooleanField(default=False)
	def __str__(self):
		try:
			rval=self.client.email
			if not rval:return self.id
			return rval
		except:
			return self.id

class StoreSite(models.Model):
	RED_GRADE_CHOICES=(
		('A','A Excellent'),
		('B','B Better'),
		('C','C Good'),
		('D','D Fair'),
		('E','E Lacking'),
	)
	name = models.CharField(max_length=100)
	create_date = models.DateTimeField('Creation Date',blank=True,null=True, auto_now_add=True)#,
	project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="store-sites", null=True)

	site_locator = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Site Locator", related_name="SL", null=True, blank=True)
	lease_negotiator = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Lease Negotiator", related_name="CSM", null=True, blank=True)#i.e. CSM
	site_status = models.ForeignKey(SiteStatus, on_delete=models.CASCADE, verbose_name="sctatus",related_name="sc_status", null=True, blank=True)

	grade = models.IntegerField(null=True, blank=True)
	red_grade = models.CharField(max_length=1, default='E', null=True, blank=True, choices=RED_GRADE_CHOICES)#red=Real Estate Director
	age = models.IntegerField(null=True, blank=True)
	seen_from_street = models.BooleanField(null=True,default=False)
	facing_street = models.BooleanField(null=True,default=False)
	vacancies = models.BooleanField(null=True,default=False)
	pylon_available = models.BooleanField(null=True,default=False)
	center_type = models.CharField(null=True, max_length=100, blank=True)
	anchor = models.CharField(null=True, blank=True, max_length=100)
	traffic_a = models.CharField(null=True, blank=True, max_length=100)
	traffic_a_num = models.IntegerField(null=True, blank=True)
	traffic_b = models.CharField(null=True, blank=True, max_length=100)
	traffic_b_num = models.IntegerField(null=True, blank=True)
	anchor = models.CharField(null=True, blank=True, max_length=100)
	distance_from_client = models.FloatField(null=True, blank=True)
	anchor_walking_distance = models.CharField(max_length=100, null=True, blank=True)
	escape_days = models.IntegerField(null=True, blank=True)
	average_income = models.IntegerField(null=True, blank=True)
	gross_income_projection = models.IntegerField(null=True, blank=True)
	population_1m = models.IntegerField(null=True, blank=True)
	population_3m = models.IntegerField(null=True, blank=True)
	population_5m = models.IntegerField(null=True, blank=True)
	avg_hh_income_1m = models.IntegerField(null=True, blank=True)
	address = models.CharField(max_length=64)
	city = models.CharField(max_length=32)
	state = models.CharField(max_length=2, choices=state_choices)
	zip_code = models.CharField(max_length=10)
	sl_comment = models.TextField(null=True, blank=True)
	tenant_improvements = models.FloatField(null=True, blank=True)
	lat = models.FloatField(null=True, blank=True)
	lng = models.FloatField(null=True, blank=True)
	target_rent = models.FloatField(null=True, blank=True)
	#all_in = models.FloatField(null=True, blank=True)
	mark_read = models.BooleanField(null=True,default=False)
	#
	sqft = models.IntegerField(null=True, blank=True)

	rba=models.IntegerField(null=True, blank=True)
	rent_sf_yr=models.CharField(max_length=32, default='0',null=True,blank=True)
	total_sf_available=models.IntegerField(null=True, blank=True)
	#
	r_comp=models.IntegerField(null=True,blank=True)
	#
	broker_company=models.CharField(max_length=64, default='0',blank=True, null=True)
	broker_contact=models.CharField(max_length=32, default='0',blank=True, null=True)
	broker_phone=models.CharField(max_length=32, default='0',blank=True, null=True)
	broker_cell=models.CharField(max_length=32, default='0',blank=True, null=True)
	broker_email=models.CharField(max_length=64, default='email',blank=True, null=True)
	broker_address = models.CharField(max_length=64,default='',blank=True,null=True)
	broker_city = models.CharField(max_length=32,default='', null=True)
	broker_state = models.CharField(max_length=2,default='', choices=state_choices)
	broker_zipcode = models.CharField(max_length=10,default='', null=True)
	#
	rawsite_note = models.CharField(max_length=64,null=True, blank=True,default='')
	director_note = models.CharField(max_length=64,null=True, blank=True,default='')

def storage_path(instance,fname):
	try:
		#fs=FileSystemStorage(location=user_media_dir)
		#spath='lost_and_found/{}'.format(fname)
		#using author_info=email as definitive owner for account determination, thus storage subdir ...
		#project=Project.objects.get(username=instance.storesite)
		#project_id=project.id
		spath='{}/{}'.format(instance.storesite.id,fname)
		return spath
	except:logging.info(sys.exc_info())
	return 'lost_and_found/{}'.format(fname)

class SiteImage(models.Model):#the activity.data (pages) points to the image file url
	storesite = models.ForeignKey(StoreSite, related_name='images', on_delete=models.CASCADE, null=True)
	image_file = models.ImageField(upload_to=storage_path, null=True, blank=True)#symlink to /var/www/uploads
	def __str__(self):
		return self.image_file.url
