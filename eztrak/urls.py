from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from eztrak import views

# API endpoints
urlpatterns = format_suffix_patterns([
	path('api/', views.api_root),
	path('api/projects/',views.ProjectList.as_view(),name='project-list'),
	path('api/projects/<int:pk>/',views.ProjectDetail.as_view(),name='project-detail'),
	path('api/clients/',views.ClientList.as_view(),name='client-list'),
	path('api/clients/<int:pk>/',views.ClientDetail.as_view(),name='client-detail'),
	path('api/employees/',views.EmployeeList.as_view(),name='employee-list'),
	path('api/employees/<int:pk>/',views.EmployeeDetail.as_view(),name='employee-detail'),
	path('api/store_sites/',views.StoreSiteList.as_view(),name='storesite-list'),
	path('api/store_sites/<int:pk>/',views.StoreSiteDetail.as_view(),name='storesite-detail'),
	path('api/site_images/',views.SiteImageList.as_view(),name='siteimage-list'),
	path('api/site_images/<int:pk>/',views.SiteImageDetail.as_view(),name='siteimage-detail'),
])
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
	path('home/', views.home),
	path('users/',views.UserList.as_view(),name='user-list'),
	path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail'),
"""
