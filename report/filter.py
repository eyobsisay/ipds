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
from project_Appriasal.models import ProjectAppraisal,ProjectAppraisalEvaluation,projectImplementationAndPlan
from project_implementation.models import ProjectImplementations

class ProjectAppriasalFilter(django_filters.FilterSet):

    class Meta:
        model= ProjectAppraisal
        fields=['project_name',
        'project_supervising_sector',
        'project_owner','project_outcome',
        'project_intended_beneficiaries',
        'project_regions','project_site',
        'project_finance',
        'project_duration','created_date',
        'project_finance__investment_cost_etb',
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

    class Meta:
        model= ProjectImplementations
        fields=['project',
        'project_starting_date',
        'project_ending_date',
        'project_consultant_type',
        'consultant_advisor_name',
        'project_contractor_type',
        'contractor_name',
        'project_measurement',
        'measurement_value',
        'project_work_status',
        'project_financial_status',
        'project_remark',
        'project_work_status__work_status',
        'project_work_status__current_budget_year',
        'project_work_status__pre_b_year_work_perf_in_percent',
        'project_work_status__physical_work_plan_year',
        'project_work_status__project_work_pane_in_four_quarter',
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

        'project_remark__budget_year_obstacle',
        'project_remark__project_total_limitation',
        

        ]


