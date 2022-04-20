from django.contrib import admin
from eztrak.models import *

class ProjectAdmin(admin.ModelAdmin):
	model=Project
	list_display=('id','all_clients')
	readonly_fields=[]
	search_fields=('clients',)

	def all_clients(self,obj):
		pcs=ProjectClient.objects.filter(project_id=obj.id)
		rval=None
		for pc in pcs:
			if rval==None:
				rval='{}'.format(pc.client.email)
			else:
				rval='{}<br>{}'.format(rval,pc.client.email)
		try:return format_html(rval)
		except:return rval
admin.site.register(Project,ProjectAdmin)

class EmployeeAdmin(admin.ModelAdmin):
	model=Employee
	list_display = ('id','become','user')
	#search_fields = ('is_manager','is_salesrep','is_finance','is_realestate','is_buildout','is_sitelocator','is_csm','is_leasingmanager','is_accounting','is_extendedmanager','is_fundingadvisor',)
	raw_id_fields = ('user',)
	search_fields=('user__username','user__last_name','user__first_name','user__email',)
	#list_filter=(HasSuperuserFilter,'autodialer','active','is_salesrep','is_sitelocator','is_leasingmanager','is_lease_negotiator','is_manager','is_fundingadvisor','is_finance','is_realestate','is_buildout','is_accounting','is_csm','is_accounting','is_extendedmanager')
	#readonly_fields = ['user']

	def become(self,obj):
		rval=""
		project_url="/become/%d/"%(obj.id)#EID=3=Bruce
		rval+="<a href='%s'>%s</a>"%(project_url,'Become Employee')
		return format_html(rval)

	def email(self,obj):
		return obj.user.email
	def last_name(self,obj):
		return obj.user.last_name
	def first_name(self,obj):
		return obj.user.first_name
	def __str__(self,obj):
		return '{}, {}'.format(obj.user.last_name,obj.user.first_name)
admin.site.register(Employee,EmployeeAdmin)

class ClientAdmin(admin.ModelAdmin):
	model=Client
	list_display = ('id','name','become','email')
	readonly_fields=['finances',]
	search_fields = ('first_name', 'last_name','email',)
	#list_filter=('hnw',)

	def become(self,obj):
		rval=""
		project_url="/become_client/%d/"%(obj.id)#EID=3=Bruce
		rval+="<a targt='_blank' href='%s'>%s</a>"%(project_url,'Become Client')
		return format_html(rval)

	def name(self,obj):
		return '{0}, {1}'.format(obj.last_name,obj.first_name)
	def __str__(self,obj):
		return '{}, {}'.format(obj.last_name,obj.first_name)
	def score(self,obj):
		try:return obj.finances.credit_score
		except:return '{}'.format(sys.exc_info())
admin.site.register(Client,ClientAdmin)

class StoreSiteAdmin(admin.ModelAdmin):
	model=StoreSite
	list_display = ('id','name',)
	def __str__(self,obj):
		return '{}'.format(obj.name)
admin.site.register(StoreSite,StoreSiteAdmin)
