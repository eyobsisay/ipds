from faulthandler import enable
from functools import cache
from multiprocessing import context
from pickletools import read_bytes1
from sys import implementation
from django.shortcuts import render
from collections import OrderedDict

from django.db.models import Sum

from project_implementation.models import ProjectImplementationsMedia,QuarterWorkPerformance,FinancialStatus,QuarterFinancialPerformance,QuarterFinancialPlan,QuarterWorkPerformance

# Create your views here.
from .fusioncharts import *
from django.shortcuts import render
from project_Appriasal.models import ProjectAppraisal,projectImplementationAndPlan,ProjectAppraisalEvaluation,ProjectAppraisalMedia
from report.filter import *
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
global pagination_no
pagination_no=2
def index(request):
    templet_name='report/index.html'
    context={}

    return render(request,templet_name,context)
    
# start of search functions    
def search(request):
    qs=ProjectAppraisal.objects.filter(is_active=True)
    filter = ProjectAppriasalFilter(request.GET, queryset=qs)
    
    return filter


def search_implementation(request):
    qs=ProjectImplementations.objects.all()
    filter = ProjectImplementationsFilter(request.GET, queryset=qs)
    
    return filter
def  search_project_appraisal_evaluation(request):
    qs=ProjectAppraisalEvaluation.objects.all()
    filter=ProjectAppraisalEvaluationFilter(request.GET, queryset=qs)
    return filter

def  search_project_implementation_and_plan(request):
    qs=projectImplementationAndPlan.objects.all()
    filter=projectImplementationAndPlanFilter(request.GET, queryset=qs)
    return filter

def search_project_appraisal_media_with_quarter(request):
    qs=ProjectAppraisalMedia.objects.all()
    filter=ProjectAppraisalMediaFilter(request.GET, queryset=qs)
    return filter  
def search_project_implementations_media_with_quarter(request):
    qs=ProjectImplementationsMedia.objects.all()
    filter=ProjectImplementationsMediaFilter(request.GET, queryset=qs)
    return filter       
# end of search functions  

def project_appraisal_detail(request,id):

    project_appraisal_detail=ProjectAppraisal.objects.get(id=id)
    return project_appraisal_detail
   
def pagination(request,filter):
    page = request.GET.get('page', 1)

    paginator = Paginator(filter.qs, pagination_no)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)  
    return data 
def pagination_image(request,filter):
    page = request.GET.get('page', 1)

    paginator = Paginator(filter.qs, pagination_no)
    try:
        data_image = paginator.page(page)
    except PageNotAnInteger:
        data_image = paginator.page(1)
    except EmptyPage:
        data_image = paginator.page(paginator.num_pages)  
    return data_image  
def pagination_video(request,filter):
    page = request.GET.get('page', 1)

    paginator = Paginator(filter.qs, pagination_no)
    try:
        data_video = paginator.page(page)
    except PageNotAnInteger:
        data_video = paginator.page(1)
    except EmptyPage:
        data_video = paginator.page(paginator.num_pages)  
    return data_video            
# start of project appraisal view 
def project_information_report(request):
    filter=search(request)
    # page = request.GET.get('page', 1)

    data=pagination(request,filter)
    
    templet_name='report/project_appraisal/project_information_report.html'
    context={'filter':filter,
    'data':data}

    return render(request,templet_name,context)  

def project_information_report_detail(request,id):
    project_information_detail=ProjectAppraisal.objects.get(id=id)
    templet_name='report/project_appraisal/project_information_report_detail.html'
    rs=ProjectAppraisalEvaluation.objects.get(project_appraisal_id=project_information_detail.id)
    rs2=projectImplementationAndPlan.objects.get(project_appraisal_id=project_information_detail.id)

    

    context={'project_information_detail':project_information_detail,
    'rs':rs,
    'rs2':rs2,
    }
    
    # return render(request, 'index.html', {'output': column2D.render()})
    return render(request,templet_name,context)       

def project_financial_report(request):
    filter=search(request)
    data=pagination(request,filter)
    templet_name='report/project_appraisal/project_financial_report.html'
    context={'filter':filter,
    'data':data}
    return render(request,templet_name,context)

def project_financial_report_detail(request,id):
    project_financial_report_detail=project_appraisal_detail(request,id)
    rs=ProjectAppraisalEvaluation.objects.get(project_appraisal_id=project_financial_report_detail.id)
    rs2=projectImplementationAndPlan.objects.get(project_appraisal_id=project_financial_report_detail.id)

    
    templet_name='report/project_appraisal/project_financial_report_detail.html' 
    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    dataSource = OrderedDict()
    chartConfig =OrderedDict()
    chartConfig["caption"] = "Project Investment  cost"
    chartConfig["subCaption"] = "in Million"
    chartConfig["xAxisName"] = "Birr type"
    chartConfig["yAxisName"] = "Investment cost"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    dataSource["data"].append({"label": 'Investment in USD', "value": project_financial_report_detail.project_finance.investment_cost_etb})
    dataSource["data"].append({"label": 'Investment in ETB', "value": project_financial_report_detail.project_finance.investment_cost_usd})
    column2D  = FusionCharts("column2d", "myFirstChart", "600", "400", "chart-1", "json", dataSource)
    chartConfig1 =OrderedDict()
    chartConfig1["caption"] = "Joint finance source "
    chartConfig1["subCaption"] = "in Million"
    chartConfig1["xAxisName"] = "Country"
    chartConfig1["yAxisName"] = "Birr type"
    chartConfig1["numberSuffix"] = ""
    chartConfig1["theme"] = "fusion"
    
    data_source_joint_finance_source=OrderedDict()
    data_source_joint_finance_source["chart"]=chartConfig1
    data_source_joint_finance_source["data"]=[]
    data_source_joint_finance_source["data"].append({"label": project_financial_report_detail.project_finance.project_source_detail.jointly.name_of_country.name, "value": project_financial_report_detail.project_finance.project_source_detail.jointly.abroad_share_etb})
    data_source_joint_finance_source["data"].append({"label": 'Inland', "value": project_financial_report_detail.project_finance.project_source_detail.jointly.inland_share_etb})
    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    data_source_joint_finance_source_column2D  = FusionCharts("column2d", "secondChart", "600", "400", "chart-2", "json", data_source_joint_finance_source)

    context={'project_financial_report_detail':project_financial_report_detail,
    'output' : column2D .render(), 
    'chartTitle': 'Pie 3D Chart',
    'rs1':rs2,
    'rs2':rs,
    'output2' : data_source_joint_finance_source_column2D.render()}
    
    return render(request,templet_name,context)

def project_evaluation_report(request):
    filter=search_project_appraisal_evaluation(request)
    filter2=search_project_implementation_and_plan(request)
    data=pagination(request,filter)
    data2=pagination(request,filter2)
    templet_name='report/project_appraisal/project_evaluation_report.html'
    filter_list = zip(filter.qs, filter2.qs)
    data_list=zip(data,data2)
    context={'filter_list':filter_list,
    'filter':filter,
    'filter2':filter2,
    'data_list':data_list}

    return render(request,templet_name,context)    

def project_evaluation_report_detail(request,evaluation_id,plan_id):
    Project_appraisal_evaluation=ProjectAppraisalEvaluation.objects.get(id=evaluation_id)
    project_implementation_and_plan=projectImplementationAndPlan.objects.get(id=plan_id)
    templet_name='report/project_appraisal/project_evaluation_report_detail.html'
    context={'Project_appraisal_evaluation':Project_appraisal_evaluation,
    'project_implementation_and_plan':project_implementation_and_plan,
    }
    return render(request,templet_name,context)        

# end of project appraisal  view

# project implementation view start
def project_evaluation_information(request):
    filter=search_implementation(request)
    data=pagination(request,filter)
    templet_name='report/project_implementation/project_evaluation_information.html'
    context={'filter':filter,
    'data':data}

    return render(request,templet_name,context)

def project_evaluation_information_detail(request,id):
    project_evaluation_information_detail=ProjectImplementations.objects.get(id=id)
    templet_name='report/project_implementation/project_evaluation_information_detail.html'
    context={'project_evaluation_information_detail':project_evaluation_information_detail}

    return render(request,templet_name,context)

def project_work_status_report(request):
    filter=search_implementation(request)
    data=pagination(request,filter)
    templet_name='report/project_implementation/project_work_status_report.html'
    context={'filter':filter,
    'data':data}

    return render(request,templet_name,context)  

def project_work_status_report_detail(request,id):
    project_work_status_report_detail=ProjectImplementations.objects.get(id=id)
    # start of quarter physical performance chart
    dataSource = OrderedDict()
    chartConfig =OrderedDict()
    chartConfig["caption"] = "Quarter physical performance"
    chartConfig["subCaption"] = "in %"
    chartConfig["xAxisName"] = "Quarter"
    chartConfig["yAxisName"] = "Percent"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    dataSource["data"].append({"label": 'First Quarter', "value": project_work_status_report_detail.project_work_status.project_work_performance_quarter.first_quarter})
    dataSource["data"].append({"label": 'Second Quarter', "value":project_work_status_report_detail.project_work_status.project_work_performance_quarter.second_quarter})
    dataSource["data"].append({"label": 'Third Quarter', "value": project_work_status_report_detail.project_work_status.project_work_performance_quarter.third_quarter})
    dataSource["data"].append({"label": 'Four Quarter', "value": project_work_status_report_detail.project_work_status.project_work_performance_quarter.fourth_quarter})
    
    column2D  = FusionCharts("column2d", "myFirstChart", "600", "400", "chart-1", "json", dataSource)
# end of quarter physical performance chart
# start of quarter physical work plan chart
    chartConfig1 =OrderedDict()
    chartConfig1["caption"] = "Quarter physical work plan"
    chartConfig1["subCaption"] = "%"
    chartConfig1["xAxisName"] = "Quarter"
    chartConfig1["yAxisName"] = "Percent"
    chartConfig1["numberSuffix"] = ""
    chartConfig1["theme"] = "fusion"
    
    data_source_quarter_work_plan=OrderedDict()
    data_source_quarter_work_plan["chart"]=chartConfig1
    data_source_quarter_work_plan["data"]=[]
    data_source_quarter_work_plan["data"].append({"label": 'First Quarter', "value": project_work_status_report_detail.project_work_status.project_work_pane_in_four_quarter.first_quarter})
    data_source_quarter_work_plan["data"].append({"label": 'Second Quarter', "value":project_work_status_report_detail.project_work_status.project_work_pane_in_four_quarter.second_quarter})
    data_source_quarter_work_plan["data"].append({"label": 'Third Quarter', "value": project_work_status_report_detail.project_work_status.project_work_pane_in_four_quarter.third_quarter})
    data_source_quarter_work_plan["data"].append({"label": 'Four Quarter', "value": project_work_status_report_detail.project_work_status.project_work_pane_in_four_quarter.fourth_quarter})
    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    data_source_quarter_work_plan_column2D  = FusionCharts("column2d", "secondChart", "600", "400", "chart-2", "json", data_source_quarter_work_plan)
# end of quarter physical work plan

# start of YTD chart
    chartConfig2 =OrderedDict()
    chartConfig2["caption"] = "YTD"
    chartConfig2["subCaption"] = "%"
    chartConfig2["xAxisName"] = "YTD"
    chartConfig2["yAxisName"] = "percent"
    chartConfig2["numberSuffix"] = ""
    chartConfig2["theme"] = "fusion"
    
    data_source_ytd=OrderedDict()
    data_source_ytd["chart"]=chartConfig2
    data_source_ytd["data"]=[]
    data_source_ytd["data"].append({"label": 'YTD physical work Plan', "value": project_work_status_report_detail.project_work_status.YTD_physical_work_plan})
    data_source_ytd["data"].append({"label": 'YTD physical work performance', "value":project_work_status_report_detail.project_work_status.YTD_physical_work_performance})
    data_source_ytd["data"].append({"label": 'YTD performance to plan Ratio', "value": project_work_status_report_detail.project_work_status.YTD_performance_to_plan_ratio})
    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    data_source_ytd_column2D  = FusionCharts("column2d", "thirdChart", "600", "400", "chart-3", "json", data_source_ytd)
# end of YTD chart
    templet_name='report/project_implementation/project_work_status_report_detail.html'
    context={'project_work_status_report_detail':project_work_status_report_detail,
    'output':column2D.render(),
    'output2':data_source_quarter_work_plan_column2D.render(),
    'output3':data_source_ytd_column2D.render()}

    return render(request,templet_name,context)  

def project_financial_status_report(request):
    filter=search_implementation(request)
    data=pagination(request,filter)
    templet_name='report/project_implementation/project_financial_status_report.html'
    context={'filter':filter,
    'data':data}

    return render(request,templet_name,context)

def project_financial_status_report_detail(request,id):
    project_financial_status_report_detail=ProjectImplementations.objects.get(id=id)
    # start of quarter physical performance chart
    dataSource = OrderedDict()
    chartConfig =OrderedDict()
    chartConfig["caption"] = "Quarter physical Financial plan"
    chartConfig["subCaption"] = "in %"
    chartConfig["xAxisName"] = "Quarter"
    chartConfig["yAxisName"] = "Percent"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    dataSource["data"].append({"label": 'First Quarter', "value": project_financial_status_report_detail.project_financial_status.quarter_financial_plan.first_quarter})
    dataSource["data"].append({"label": 'Second Quarter', "value":project_financial_status_report_detail.project_financial_status.quarter_financial_plan.second_quarter})
    dataSource["data"].append({"label": 'Third Quarter', "value": project_financial_status_report_detail.project_financial_status.quarter_financial_plan.third_quarter})
    dataSource["data"].append({"label": 'Four Quarter', "value": project_financial_status_report_detail.project_financial_status.quarter_financial_plan.fourth_quarter})
    
    column2D  = FusionCharts("column2d", "myFirstChart", "600", "400", "chart-1", "json", dataSource)
# end of quarter physical performance chart
# start of quarter physical work plan chart
    chartConfig1 =OrderedDict()
    chartConfig1["caption"] = "Quarter physical financial performance"
    chartConfig1["subCaption"] = "%"
    chartConfig1["xAxisName"] = "Quarter"
    chartConfig1["yAxisName"] = "Percent"
    chartConfig1["numberSuffix"] = ""
    chartConfig1["theme"] = "fusion"
    
    data_source_quarter_work_plan=OrderedDict()
    data_source_quarter_work_plan["chart"]=chartConfig1
    data_source_quarter_work_plan["data"]=[]
    data_source_quarter_work_plan["data"].append({"label": 'First Quarter', "value": project_financial_status_report_detail.project_financial_status.quarter_financial_plan.first_quarter})
    data_source_quarter_work_plan["data"].append({"label": 'Second Quarter', "value":project_financial_status_report_detail.project_financial_status.quarter_financial_plan.second_quarter})
    data_source_quarter_work_plan["data"].append({"label": 'Third Quarter', "value": project_financial_status_report_detail.project_financial_status.quarter_financial_plan.third_quarter})
    data_source_quarter_work_plan["data"].append({"label": 'Four Quarter', "value":project_financial_status_report_detail.project_financial_status.quarter_financial_plan.fourth_quarter})
    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    data_source_quarter_work_financial_column2D  = FusionCharts("column2d", "secondChart", "600", "400", "chart-2", "json", data_source_quarter_work_plan)
# end of quarter physical work plan

# start of YTD chart
    chartConfig2 =OrderedDict()
    chartConfig2["caption"] = "YTD financial"
    chartConfig2["subCaption"] = "%"
    chartConfig2["xAxisName"] = "YTD"
    chartConfig2["yAxisName"] = "percent"
    chartConfig2["numberSuffix"] = ""
    chartConfig2["theme"] = "fusion"
    
    data_source_ytd=OrderedDict()
    data_source_ytd["chart"]=chartConfig2
    data_source_ytd["data"]=[]
    data_source_ytd["data"].append({"label": 'YTD physical work financial', "value":project_financial_status_report_detail.project_financial_status.YTD_financial_work_plan})
    data_source_ytd["data"].append({"label": 'YTD physical work financial performance', "value":project_financial_status_report_detail.project_financial_status.YTD_financial_work_performance})
    data_source_ytd["data"].append({"label": 'YTD performance to plan  financial Ratio', "value": project_financial_status_report_detail.project_financial_status.YTD_financial_performance_to_plan_ratio})
    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    data_source_ytd_financial_column2D  = FusionCharts("column2d", "thirdChart", "600", "400", "chart-3", "json", data_source_ytd)
# end of YTD chart
    templet_name='report/project_implementation/project_financial_status_report_detail.html'
    
    context={'project_financial_status_report_detail':project_financial_status_report_detail,
     'output':column2D.render(),
    'output2':data_source_quarter_work_financial_column2D.render(),
    'output3':data_source_ytd_financial_column2D.render()
    
    }

    return render(request,templet_name,context)
def project_remark_report(request):
    filter=search_implementation(request)
    data=pagination(request,filter)
    templet_name='report/project_implementation/project_remark_report.html'
    context={'filter':filter,
    'data':data}

    return render(request,templet_name,context) 

def project_remark_report_detail(request,id):
    project_remark_report_detail=ProjectImplementations.objects.get(id=id)
    templet_name='report/project_implementation/project_remark_report_detail.html'
    context={'project_remark_report_detail':project_remark_report_detail}

    return render(request,templet_name,context) 

# end fo appraisal report
def all_details(request,id):
  templet_name='report/all_in_one_detail.html'
  project_appraisal_detail=ProjectAppraisal.objects.get(id=id)
  
  
  try:
    project_implementation_detail=ProjectImplementations.objects.get(project_id=id)
  except ProjectImplementations.DoesNotExist:
    project_implementation_detail=None

  try:
   Project_appraisal_evaluation=ProjectAppraisalEvaluation.objects.get(project_appraisal_id=id)
  except ProjectAppraisalEvaluation.DoesNotExist:
    Project_appraisal_evaluation=None
  try:
   project_implementation_and_plan=projectImplementationAndPlan.objects.get(project_appraisal_id=id)
  except projectImplementationAndPlan.DoesNotExist:
    project_implementation_and_plan=None    

  context={'project_appraisal_detail':project_appraisal_detail,
  'project_implementation_detail':project_implementation_detail,
  'Project_appraisal_evaluation':Project_appraisal_evaluation,
  'project_implementation_and_plan':project_implementation_and_plan}
  return render(request,templet_name,context)
def dashboard(request):
    templet_name='report/dashboard.html'
    project_implementations=ProjectImplementations.objects.all()
    project_appraisal = ProjectAppraisal.objects.all()
    project_implementation_plan=projectImplementationAndPlan.objects.all()
    project_appraisal_evaluation=ProjectAppraisalEvaluation.objects.all()

    project_count_data={
        'all_project':project_appraisal.count(),
        'project_on_implementation':project_implementations.count(),
        'Accepted_project':project_appraisal_evaluation.filter(appraisal_result__result_name="Accepted").count(),
        'unaccepted_project':project_appraisal_evaluation.filter(appraisal_result__result_name="Unaccepted").count(),
        'not_evaluated_project':project_appraisal.count()-project_appraisal_evaluation.count()
        

    }
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Project Investment cost",
            # "subCaption": "Harry's SuperMart",
            "xAxisName": "Projects",
            "yAxisName": "Investment cost (Birr)",
            "numberPrefix": "",
            "theme": "fusion"
        }
    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in project_appraisal:
      data = {}
      data['label'] = key.project_name
      data['value'] = key.project_finance.investment_cost_etb
      dataSource['data'].append(data)
    project_investment_cost_etb={

    }
    column2D  = FusionCharts("column2d", "myFirstChart", "600", "400", "chart-1", "json", dataSource)


    # project owner investment  cost Chart
    data_of_project_owner = {}
    data_of_project_owner['chart'] = { 
        "caption": "Project Owner total Investment cost",
            # "subCaption": "Harry's SuperMart",
            "xAxisName": "Projects",
            "yAxisName": "Investment cost (Birr)",
            "numberPrefix": "",
            "theme": "fusion"
        }
    data_of_project_owner['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    project_appraisal_owners = (ProjectAppraisal.objects.values('project_owner__owner_name').order_by('project_owner__owner_name').annotate(total_investment=Sum('project_finance__investment_cost_etb')))
    print('-------------------')
    print(project_appraisal_owners)
   
    for key in project_appraisal_owners:
        data = {}
        data['label'] =key['project_owner__owner_name']
        data['value'] = key['total_investment']
        data_of_project_owner['data'].append(data)
    data_of_project_owner_column2D  = FusionCharts("column2d", "secondChart", "600", "400", "chart-2", "json", data_of_project_owner)
    
 # end project owner investment  cost Chart
# start total sum of quarter finance data

    dataSource_in_finance_quarter = OrderedDict()
    chartConfig2 =OrderedDict()
    chartConfig2["caption"] = "Quarter finance Performance data"
    chartConfig2["subCaption"] = "in %"
    chartConfig2["numberSuffix"] = ""
    chartConfig2["theme"] = "fusion"

    dataSource_in_finance_quarter["chart"] = chartConfig2
    dataSource_in_finance_quarter["data"] = []
    financial_plan_first_quarter=0
    financial_plan_second_quarter=0
    financial_plan_third_quarter=0
    financial_plan_forth_quarter=0
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    for qs in QuarterFinancialPerformance.objects.all():
        financial_plan_first_quarter=+ qs.first_quarter
        financial_plan_second_quarter=+ qs.second_quarter
        financial_plan_third_quarter=+ qs.third_quarter
        financial_plan_forth_quarter=+ qs.fourth_quarter

    dataSource_in_finance_quarter["data"].append({"label": 'First Quarter', "value": financial_plan_first_quarter})
    dataSource_in_finance_quarter["data"].append({"label": 'Second Quarter', "value":financial_plan_second_quarter})
    dataSource_in_finance_quarter["data"].append({"label": 'Third Quarter', "value": financial_plan_third_quarter})
    dataSource_in_finance_quarter["data"].append({"label": 'Forth Quarter', "value": financial_plan_forth_quarter})
    dataSource_in_finance_quarter_column2D  = FusionCharts("pie3d", "fourChart", "600", "400", "chart-4", "json", dataSource_in_finance_quarter)

# end  total sum of quarter finance data

# start total sum of quarter work performance data

    dataSource_in_works_performance_quarter = OrderedDict()
    chartConfig3 =OrderedDict()
    chartConfig3["caption"] = "Quarter work performance data"
    chartConfig3["subCaption"] = "in %"
    chartConfig3["numberSuffix"] = ""
    chartConfig3["theme"] = "fusion"

    dataSource_in_works_performance_quarter["chart"] = chartConfig3
    dataSource_in_works_performance_quarter["data"] = []
    work_performance_plan_first_quarter=0
    work_performance_second_quarter=0
    work_performances_third_quarter=0
    work_performance_forth_quarter=0
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    for qs in QuarterWorkPerformance.objects.all():
        work_performance_plan_first_quarter=+ qs.first_quarter
        work_performance_second_quarter=+ qs.second_quarter
        work_performances_third_quarter=+ qs.third_quarter
        work_performance_forth_quarter=+ qs.fourth_quarter

    dataSource_in_works_performance_quarter["data"].append({"label": 'First Quarter', "value": work_performance_plan_first_quarter})
    dataSource_in_works_performance_quarter["data"].append({"label": 'Second Quarter', "value":work_performance_second_quarter})
    dataSource_in_works_performance_quarter["data"].append({"label": 'Third Quarter', "value": work_performances_third_quarter})
    dataSource_in_works_performance_quarter["data"].append({"label": 'Forth Quarter', "value": work_performance_forth_quarter})
    dataSource_in_works_performance_quarter_column2D  = FusionCharts("doughnut3d", "fiveChart", "600", "400", "chart-5", "json", dataSource_in_works_performance_quarter)
    
    dataSource_in_ytd = OrderedDict()
    chartConfig5 =OrderedDict()
    chartConfig5["caption"] = "YTD"
    chartConfig5["subCaption"] = "in %"
    chartConfig5["numberSuffix"] = ""
    chartConfig5["theme"] = "fusion"

    dataSource_in_ytd["chart"] = chartConfig5
    dataSource_in_ytd["data"] = []
    YTD_financial_work_plan=0
    YTD_financial_work_performance=0
    YTD_financial_performance_to_plan_ratio=0
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    for qs in FinancialStatus.objects.all():
        YTD_financial_work_plan=+ qs.YTD_financial_work_plan
        YTD_financial_work_performance=+ qs.YTD_financial_work_performance
        YTD_financial_performance_to_plan_ratio=+ qs.YTD_financial_performance_to_plan_ratio
       

    dataSource_in_ytd["data"].append({"label": 'YTD financial plan Quarter', "value": YTD_financial_work_plan})
    dataSource_in_ytd["data"].append({"label": 'YTD financial plan Quarter', "value":YTD_financial_work_performance})
    dataSource_in_ytd["data"].append({"label": 'YTD financial plan Quarter', "value": YTD_financial_performance_to_plan_ratio})
    dataSource_in_ytd_column2D  = FusionCharts("pie3d", "sixChart", "600", "400", "chart-6", "json", dataSource_in_ytd)
    
    
    
    
    
    # project site
    data_of_project_site = {}
    data_of_project_site['chart'] = { 
        "caption": "Project on site",
            # "subCaption": "Harry's SuperMart",
            "xAxisName": "Site",
            "yAxisName": "project Number",
            "numberPrefix": "",
            "theme": "fusion"
        }
    data_of_project_site['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    project_appraisal_site = (ProjectAppraisal.objects.values('project_site__region__name').order_by('project_site__region__name').annotate(total=Count('project_finance__investment_cost_etb')))

    print('--------------------------test---------------')
    print(dataSource_in_finance_quarter)
    for key in project_appraisal_site:
        data = {}
        data['label'] =key['project_site__region__name']
        data['value'] = key['total']
        data_of_project_site['data'].append(data)
   
    data_of_project_site_column2D  = FusionCharts("column2d", "thirdChart", "600", "400", "chart-3", "json", data_of_project_site)
   
   
   
    
    context={
        'project_count_data':project_count_data,
        'output':column2D.render(),
        'output2':data_of_project_owner_column2D.render(),
        'output3':data_of_project_site_column2D.render(),
        'output4':dataSource_in_finance_quarter_column2D.render(),
        'output5':dataSource_in_works_performance_quarter_column2D.render(),
        'output6':dataSource_in_ytd_column2D.render(),
        
    } 
    return render(request,templet_name,context) 



def gallery(request,id):
    filter=search_project_appraisal_media_with_quarter(request)
    data_image=pagination_image(request,filter)
    data_video=pagination_video(request,filter)
    templet_name='report/gallery.html'
    project=ProjectAppraisal.objects.get(id=id)
    context={'data_image':data_image,
    'project':project,
    'filter':filter,
    'data_video':data_video}

    return render(request,templet_name,context) 
def gallery_implementation(request,id):
    filter=search_project_implementations_media_with_quarter(request)
    project=ProjectImplementations.objects.get(id=id)
    data_image=pagination_image(request,filter)
    data_video=pagination_video(request,filter)
    templet_name='report/gallery.html'
    
    context={'data_image':data_image,
    'filter':filter,
    'data_video':data_video,
    'project':project}

    return render(request,templet_name,context) 
       

def sample():
    project_implementations=ProjectImplementations.objects.all()
    project_appraisal = ProjectAppraisal.objects.all()
    project_implementation_plan=projectImplementationAndPlan.objects.all()
    project_appraisal_evaluation=ProjectAppraisalEvaluation.objects.all()

    project_count_data={
        'all_project':project_appraisal.count(),
        'project_on_implementation':project_implementations.count(),
        'Accepted_project':project_appraisal_evaluation.filter(appraisal_result__result_name="Accepted").count(),
        'unaccepted_project':project_appraisal_evaluation.filter(appraisal_result__result_name="Unaccepted").count(),
        'not_evaluated_project':project_appraisal.count()-project_appraisal_evaluation.count()
        

    }
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Project Investment cost",
            # "subCaption": "Harry's SuperMart",
            "xAxisName": "Projects",
            "yAxisName": "Investment cost (Birr)",
            "numberPrefix": "",
            "theme": "fusion"
        }
    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in project_appraisal:
      data = {}
      data['label'] = key.project_name
      data['value'] = key.project_finance.investment_cost_etb
      dataSource['data'].append(data)
    project_investment_cost_etb={

    }
    column2D  = FusionCharts("column2d", "myFirstChart", "600", "400", "chart-1", "json", dataSource)


    # project owner investment  cost Chart
    data_of_project_owner = {}
    data_of_project_owner['chart'] = { 
        "caption": "Project Owner total Investment cost",
            # "subCaption": "Harry's SuperMart",
            "xAxisName": "Projects",
            "yAxisName": "Investment cost (Birr)",
            "numberPrefix": "",
            "theme": "fusion"
        }
    data_of_project_owner['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    project_appraisal_owners = (ProjectAppraisal.objects.values('project_owner__owner_name').order_by('project_owner__owner_name').annotate(total_investment=Sum('project_finance__investment_cost_etb')))
    print('-------------------')
    print(project_appraisal_owners)
   
    for key in project_appraisal_owners:
        data = {}
        data['label'] =key['project_owner__owner_name']
        data['value'] = key['total_investment']
        data_of_project_owner['data'].append(data)
    data_of_project_owner_column2D  = FusionCharts("column2d", "secondChart", "600", "400", "chart-2", "json", data_of_project_owner)
    
 # end project owner investment  cost Chart
# start total sum of quarter finance data

    dataSource_in_finance_quarter = OrderedDict()
    chartConfig2 =OrderedDict()
    chartConfig2["caption"] = "Quarter finance Performance data"
    chartConfig2["subCaption"] = "in %"
    chartConfig2["numberSuffix"] = ""
    chartConfig2["theme"] = "fusion"

    dataSource_in_finance_quarter["chart"] = chartConfig2
    dataSource_in_finance_quarter["data"] = []
    financial_plan_first_quarter=0
    financial_plan_second_quarter=0
    financial_plan_third_quarter=0
    financial_plan_forth_quarter=0
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    for qs in QuarterFinancialPerformance.objects.all():
        financial_plan_first_quarter=+ qs.first_quarter
        financial_plan_second_quarter=+ qs.second_quarter
        financial_plan_third_quarter=+ qs.third_quarter
        financial_plan_forth_quarter=+ qs.fourth_quarter

    dataSource_in_finance_quarter["data"].append({"label": 'First Quarter', "value": financial_plan_first_quarter})
    dataSource_in_finance_quarter["data"].append({"label": 'Second Quarter', "value":financial_plan_second_quarter})
    dataSource_in_finance_quarter["data"].append({"label": 'Third Quarter', "value": financial_plan_third_quarter})
    dataSource_in_finance_quarter["data"].append({"label": 'Forth Quarter', "value": financial_plan_forth_quarter})
    dataSource_in_finance_quarter_column2D  = FusionCharts("pie3d", "fourChart", "600", "400", "chart-4", "json", dataSource_in_finance_quarter)

# end  total sum of quarter finance data

# start total sum of quarter work performance data

    dataSource_in_works_performance_quarter = OrderedDict()
    chartConfig3 =OrderedDict()
    chartConfig3["caption"] = "Quarter work performance data"
    chartConfig3["subCaption"] = "in %"
    chartConfig3["numberSuffix"] = ""
    chartConfig3["theme"] = "fusion"

    dataSource_in_works_performance_quarter["chart"] = chartConfig3
    dataSource_in_works_performance_quarter["data"] = []
    work_performance_plan_first_quarter=0
    work_performance_second_quarter=0
    work_performances_third_quarter=0
    work_performance_forth_quarter=0
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    for qs in QuarterWorkPerformance.objects.all():
        work_performance_plan_first_quarter=+ qs.first_quarter
        work_performance_second_quarter=+ qs.second_quarter
        work_performances_third_quarter=+ qs.third_quarter
        work_performance_forth_quarter=+ qs.fourth_quarter

    dataSource_in_works_performance_quarter["data"].append({"label": 'First Quarter', "value": work_performance_plan_first_quarter})
    dataSource_in_works_performance_quarter["data"].append({"label": 'Second Quarter', "value":work_performance_second_quarter})
    dataSource_in_works_performance_quarter["data"].append({"label": 'Third Quarter', "value": work_performances_third_quarter})
    dataSource_in_works_performance_quarter["data"].append({"label": 'Forth Quarter', "value": work_performance_forth_quarter})
    dataSource_in_works_performance_quarter_column2D  = FusionCharts("doughnut3d", "fiveChart", "600", "400", "chart-5", "json", dataSource_in_works_performance_quarter)
    
    dataSource_in_ytd = OrderedDict()
    chartConfig5 =OrderedDict()
    chartConfig5["caption"] = "YTD"
    chartConfig5["subCaption"] = "in %"
    chartConfig5["numberSuffix"] = ""
    chartConfig5["theme"] = "fusion"

    dataSource_in_ytd["chart"] = chartConfig5
    dataSource_in_ytd["data"] = []
    YTD_financial_work_plan=0
    YTD_financial_work_performance=0
    YTD_financial_performance_to_plan_ratio=0
    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    for qs in FinancialStatus.objects.all():
        YTD_financial_work_plan=+ qs.YTD_financial_work_plan
        YTD_financial_work_performance=+ qs.YTD_financial_work_performance
        YTD_financial_performance_to_plan_ratio=+ qs.YTD_financial_performance_to_plan_ratio
       

    dataSource_in_ytd["data"].append({"label": 'YTD financial plan Quarter', "value": YTD_financial_work_plan})
    dataSource_in_ytd["data"].append({"label": 'YTD financial plan Quarter', "value":YTD_financial_work_performance})
    dataSource_in_ytd["data"].append({"label": 'YTD financial plan Quarter', "value": YTD_financial_performance_to_plan_ratio})
    dataSource_in_ytd_column2D  = FusionCharts("pie3d", "sixChart", "600", "400", "chart-6", "json", dataSource_in_ytd)
    
    
    
    
    
    # project site
    data_of_project_site = {}
    data_of_project_site['chart'] = { 
        "caption": "Project on site",
            # "subCaption": "Harry's SuperMart",
            "xAxisName": "Site",
            "yAxisName": "project Number",
            "numberPrefix": "",
            "theme": "fusion"
        }
    data_of_project_site['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    project_appraisal_site = (ProjectAppraisal.objects.values('project_site__region__name').order_by('project_site__region__name').annotate(total=Count('project_finance__investment_cost_etb')))

    print('--------------------------test---------------')
    print(dataSource_in_finance_quarter)
    for key in project_appraisal_site:
        data = {}
        data['label'] =key['project_site__region__name']
        data['value'] = key['total']
        data_of_project_site['data'].append(data)
   
    data_of_project_site_column2D  = FusionCharts("column2d", "thirdChart", "600", "400", "chart-3", "json", data_of_project_site)
   
   
   
    
    context={
        'project_count_data':project_count_data,
        'output':column2D.render(),
        'output2':data_of_project_owner_column2D.render(),
        'output3':data_of_project_site_column2D.render(),
        'output4':dataSource_in_finance_quarter_column2D.render(),
        'output5':dataSource_in_works_performance_quarter_column2D.render(),
        'output6':dataSource_in_ytd_column2D.render(),
        
    } 
    return context
def main_dashboard(request):
    last_project_appraisal=ProjectAppraisal.objects.all().order_by('-id')[:5]
    last_project_implementation=ProjectImplementations.objects.all().order_by('-id')[:5]
    sample_data=sample()
    qs=ProjectImplementations.objects.all()
    
    name_dic={}
    name_dic['category'] = []
    name_dic1= []
    name_dic2= []
    name_dic3 = []

    for q in qs:
      data={}
      data1={}
      data2={}
      data3={}
      data['label']=q.project.project_site.region.name
      data1['value']=q.project_financial_status.YTD_financial_work_performance
      data2['value']=q.project_work_status.project_work_performance_quarter.fourth_quarter

      data3['value']=q.project_financial_status.quarter_financial_performance.fourth_quarter
      name_dic['category'].append(data)
      name_dic1.append(data1)
      name_dic2.append(data2)
      name_dic3.append(data3)


    sample2={}
    sample2['chart']={

      "caption": "Analysing graph investment over completion rate",
      "subcaption": "By province",
      "yaxisname": "Investement ",
      "syaxisname": "Subsidies % of Income",
      "labeldisplay": "rotate",
      "snumbersuffix": "%",
      "scrollheight": "10",
      "numvisibleplot": "10",
      "drawcrossline": "1",
      "theme": "fusion"
    }
    sample2['categories']=[]
    sample2['dataset']=[]
    
    sample2['categories'].append(name_dic)
    # sample2['dataset'].append(name_dic1)
    sample2['dataset'].append( {"seriesname": "Ytd peformance", "plottooltext": "Investments $dataValue" ,'data':name_dic1})
    # sample2['dataset'].append(name_dic2)
    sample2['dataset'].append( {"seriesname": "project work performance rate",
                                  "renderas": "area",
                                  "showanchors": "0",
                                  "plottooltext": "project count: $dataValue",
                                  'data':name_dic3})
  
    sample2['dataset'].append( {"seriesname": "project finance performance rate %",
                                      "parentyaxis": "S",
                                      "renderas": "line",
                                      "plottooltext": "$dataValue completion rate",
                                      "showvalues": "0",
                                      'data':name_dic2})
                                

    chartObj = FusionCharts( 'scrollcombidy2d', 'ex1', '600', '400', 'chart-8', 'json',sample2 )
 
    
    context={'output8':chartObj.render(),
    'last_project_appraisal':last_project_appraisal,
    'last_project_implementation':last_project_implementation}
    context.update(sample_data)

    return render(request, 'main_dashboard.html', context)
