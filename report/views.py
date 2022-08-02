from faulthandler import enable
from sys import implementation
from django.shortcuts import render
from collections import OrderedDict

from django.db.models import Sum
# Create your views here.
from .fusioncharts import *
from django.shortcuts import render
from project_Appriasal.models import ProjectAppraisal,projectImplementationAndPlan,ProjectAppraisalEvaluation
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

   
    for key in project_appraisal_site:
        data = {}
        data['label'] =key['project_site__region__name']
        data['value'] = key['total']
        data_of_project_site['data'].append(data)
    print('---------------sire------------------')
    print(data_of_project_site)    
    data_of_project_site_column2D  = FusionCharts("column2d", "thirdChart", "600", "400", "chart-3", "json", data_of_project_site)
    context={
        'project_count_data':project_count_data,
        'output':column2D.render(),
        'output2':data_of_project_owner_column2D.render(),
        'output3':data_of_project_site_column2D.render(),


        
    }
    return render(request,templet_name,context) 
