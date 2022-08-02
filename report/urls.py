"""PMD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name='report'
urlpatterns = [
    # start of project appraisal report
    path('', views.index, name='index'),
    path('project_information_report', views.project_information_report, name='project_information_report'),
    path('project_information_report_detail/<int:id>/', views.project_information_report_detail, name='project_information_report_detail'),
    path('project_financial_report', views.project_financial_report, name='project_financial_report'),
    path('project_financial_report_detail/<int:id>/', views.project_financial_report_detail, name='project_financial_report_detail'),
    path('project_evaluation_report', views.project_evaluation_report, name='project_evaluation_report'),
    path('project_evaluation_report_detail/<int:evaluation_id>/<int:plan_id>/', views.project_evaluation_report_detail, name='project_evaluation_report_detail'),
    # path('project_address_report', views.project_address_report, name='project_address_report'),

    # end of project appraisal report

    # start of project implementation url
    path('project_evaluation_information', views.project_evaluation_information, name='project_evaluation_information'),
    path('project_evaluation_information_detail/<int:id>/', views.project_evaluation_information_detail, name='project_evaluation_information_detail'),
    path('project_work_status_report', views.project_work_status_report, name='project_work_status_report'),
    path('project_work_status_report_detail/<int:id>/', views.project_work_status_report_detail, name='project_work_status_report_detail'),
    path('project_financial_status_report', views.project_financial_status_report, name='project_financial_status_report'),
    path('project_financial_status_report_detail/<int:id>/', views.project_financial_status_report_detail, name='project_financial_status_report_detail'),
    path('project_remark_report', views.project_remark_report, name='project_remark_report'),
    path('project_remark_report_detail/<int:id>/', views.project_remark_report_detail, name='project_remark_report_detail'),
    path('dashboard>/', views.dashboard, name='dashboard'),

    
    
   
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
