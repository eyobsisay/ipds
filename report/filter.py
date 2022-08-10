from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Count
# Create your views here.
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
import datetime
from datetime import timedelta
from django import forms

import django_filters
from django_filters import rest_framework as filters
from project_Appriasal.models import ProjectAppraisal,ProjectAppraisalEvaluation,projectImplementationAndPlan,ProjectAppraisalMedia
from project_implementation.models import ProjectImplementations,ProjectImplementationsMedia

class ProjectAppriasalFilter(django_filters.FilterSet):
    project_name = django_filters.CharFilter(lookup_expr='icontains')
    # project_finance__investment_cost_etb = django_filters.NumberFilter()
    project_finance__investment_cost_etb__gt = django_filters.NumberFilter(field_name='project_finance__investment_cost_etb', lookup_expr='gt')
    # project_finance__investment_cost_etb__lt = django_filters.NumberFilter(field_name='project_finance__investment_cost_etb', lookup_expr='lt')

    class Meta:
        model= ProjectAppraisal
        fields=[
        'project_supervising_sector',
        'project_owner','project_outcome',
        'project_intended_beneficiaries',
        'project_regions','project_site__region',
        'project_duration','created_date',
        'project_finance__investment_cost_etb',
        'project_finance__investment_cost_usd',
        'project_finance__project_source_detail',
        ]
class ProjectAppraisalEvaluationFilter(django_filters.FilterSet):

    class Meta:
        model= ProjectAppraisalEvaluation
        fields=['project_appraisal__project_name',
        'arrival_date_of_project_appraisal_to_pds',
        'appraisal_result',
        'reason',
        'date_of_appraisal_result_sent',
        
        ] 
class projectImplementationAndPlanFilter(django_filters.FilterSet):

    class Meta:
        model= projectImplementationAndPlan
        fields=['project_appraisal__project_name',
        'arrival_date_of_plane_for_evaluation_pdm',
        'evaluation_result',
        'reason',
    
        ]                
class ProjectImplementationsFilter(django_filters.FilterSet):
    consultant_advisor_name = django_filters.CharFilter(lookup_expr='icontains')
    contractor_name = django_filters.CharFilter(lookup_expr='icontains')
    project_remark__budget_year_obstacle = django_filters.CharFilter(lookup_expr='icontains')
    project_remark__project_total_limitation = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model= ProjectImplementations
        fields=['project',
        'project_starting_date',
        'project_ending_date',
        'project_consultant_type',
        'project_contractor_type',
        'project_measurement',
        'measurement_value',
        'project_work_status',
        'project_financial_status',
        'project_remark',
        'project_work_status__work_status',
        'project_work_status__current_budget_year',
        'project_work_status__pre_b_year_work_perf_in_percent',
        'project_work_status__physical_work_plan_year',
        'project_work_status__project_work_pane_in_four_quarter__first_quarter',
        'project_work_status__project_work_performance_quarter',
        'project_work_status__YTD_physical_work_plan',
        'project_work_status__YTD_physical_work_performance',
        'project_work_status__YTD_performance_to_plan_ratio',
        'project_financial_status__pre_b_year_financial_performance_birr',
        'project_financial_status__budget_financial_plan',
        'project_financial_status__quarter_plan',
        'project_financial_status__quarter_financial_plan',
        'project_financial_status__quarter_financial_performance',
        'project_financial_status__quarter_financial_ratio',
        'project_financial_status__YTD_financial_work_plan',
        'project_financial_status__YTD_financial_work_performance',
        'project_financial_status__YTD_financial_performance_to_plan_ratio',

       
        

        ]

class ProjectAppraisalMediaFilter(django_filters.FilterSet):

    class Meta:
        model= ProjectAppraisalMedia
        fields=['quarter',
        
       
    
        ]  

class ProjectImplementationsMediaFilter(django_filters.FilterSet):

    class Meta:
        model= ProjectImplementationsMedia
        fields=['quarter',
        'project__project_starting_date'
        
       
    
        ]  
