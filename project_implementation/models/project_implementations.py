from distutils.command.upload import upload
from django.db import models

from project_Appriasal.models import ProjectAppraisal

# Create your models here.
# consultant type name for option
class ConsultantType(models.Model):
    consultant_name=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.consultant_name
# measurement unit 
class Measurement(models.Model):
    measurement_name=models.CharField(max_length=100) 
    desc=models.TextField()
    si_unit= models.CharField(max_length=100) 
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.measurement_name
# status type name
class WorkStatusType(models.Model):
    status_name=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.status_name
# quarter work plan for four quarter    
class QuarterWorkPlane(models.Model):
    first_quarter=models.IntegerField(help_text="quarter year plan  in %")
    second_quarter=models.IntegerField(help_text="quarter year plan  in %")
    third_quarter=models.IntegerField(help_text="quarter year plan  in %")  
    fourth_quarter=models.IntegerField(help_text="quarter year plan  in %")
# quarter work plan for four quarter    
class QuarterWorkPerformance(models.Model):
    first_quarter=models.IntegerField(help_text="quarter year plan  in %")
    second_quarter=models.IntegerField(help_text="quarter year plan  in %")
    third_quarter=models.IntegerField(help_text="quarter year plan  in %")  
    fourth_quarter=models.IntegerField(help_text="quarter year plan  in %") 
# quarter work performance to plan ratio for four quarter    
class QuarterWorkPerformanceToPlanRatio(models.Model):
    first_quarter=models.IntegerField(help_text="quarter year plan  in %")
    second_quarter=models.IntegerField(help_text="quarter year plan  in %")
    third_quarter=models.IntegerField(help_text="quarter year plan  in %")  
    fourth_quarter=models.IntegerField(help_text="quarter year plan  in %")        
# project work status detail    
class ProjectWorkStatus(models.Model) :
    work_status=models.ForeignKey(WorkStatusType, on_delete=models.CASCADE)
    current_budget_year=models.DateField(help_text="budget year")
    pre_b_year_work_perf_in_percent=models.IntegerField(help_text="budget year financial performance in %")
    physical_work_plan_year=models.IntegerField(help_text="short description of the BUdget year's plan in %")
    project_work_pane_in_four_quarter=models.ForeignKey(QuarterWorkPlane, on_delete=models.CASCADE,help_text="short description of the quarter year's plan in number")
    project_work_performance_quarter=models.ForeignKey(QuarterWorkPerformance,on_delete=models.CASCADE,help_text="Numerical description of the quarter year performance")
    project_performance_to_plan_ratio=models.ForeignKey(QuarterWorkPerformanceToPlanRatio,on_delete=models.CASCADE,help_text="Numerical description of the quarter year performance to plan Ratio")
    YTD_physical_work_plan=models.IntegerField(help_text="project total physical plan")
    YTD_physical_work_performance=models.IntegerField(help_text="YTD physical work performance")
    YTD_performance_to_plan_ratio=models.IntegerField(help_text="total physical work performance to plan ratio")

# quarter Financial  plan for four quarter/
class QuarterFinancialPlan(models.Model):
    first_quarter=models.IntegerField(help_text="quarter year plan ")
    second_quarter=models.IntegerField(help_text="quarter year plan ")
    third_quarter=models.IntegerField(help_text="quarter year plan ")  
    fourth_quarter=models.IntegerField(help_text="quarter year plan ")
# quarter financial performance for four quarter
class QuarterFinancialPerformance(models.Model):
    first_quarter=models.IntegerField(help_text="quarter year performance  ")
    second_quarter=models.IntegerField(help_text="quarter year performance ")
    third_quarter=models.IntegerField(help_text="quarter year performance  ")  
    fourth_quarter=models.IntegerField(help_text="quarter year performance ")
# quarter financial ration for four quarter
class QuarterFinancialRatio(models.Model):
    first_quarter=models.IntegerField(help_text="quarter year performance  ")
    second_quarter=models.IntegerField(help_text="quarter year performance ")
    third_quarter=models.IntegerField(help_text="quarter year performance  ")  
    fourth_quarter=models.IntegerField(help_text="quarter year performance ")    
# financial status detail
class FinancialStatus(models.Model):
    pre_b_year_financial_performance_birr=models.IntegerField(help_text="previous budget years's financial performance in million Birr")
    budget_financial_plan=models.IntegerField(help_text=" budget years's financial plan")
    quarter_plan=models.IntegerField(help_text="Quarter plan")
    quarter_financial_plan=models.ForeignKey(QuarterFinancialPlan,on_delete=models.CASCADE)
    quarter_financial_performance=models.ForeignKey(QuarterFinancialPerformance,on_delete=models.CASCADE)
    quarter_financial_ratio=models.ForeignKey(QuarterFinancialRatio,on_delete=models.CASCADE)
    YTD_financial_work_plan=models.IntegerField(help_text="money allocated for the project until the budget year")
    YTD_financial_work_performance=models.IntegerField(help_text="Total money used until now")
    YTD_financial_performance_to_plan_ratio=models.IntegerField()
# project remark detail 
class ProjectRemark(models.Model):
    budget_year_obstacle=models.TextField()
    project_total_limitation=models.TextField()
    project_comment=models.TextField()
    project_file=models.ImageField(blank=True,null=True,upload_to='project_file/')
    def __str__(self):
        return self.budget_year_obstacle

    # project implementation detail 
class ProjectImplementations(models.Model):
    project=models.ForeignKey(ProjectAppraisal, on_delete=models.CASCADE)
    project_starting_date=models.DateTimeField()
    project_ending_date=models.DateTimeField()
    project_consultant_type=models.ForeignKey(ConsultantType,related_name="project_consultant_type" ,on_delete=models.CASCADE)
    consultant_advisor_name=models.CharField(max_length=100)
    project_contractor_type=models.ForeignKey(ConsultantType,related_name="project_contractor_type" ,on_delete=models.CASCADE)
    contractor_name=models.CharField(max_length=100)
    project_measurement=models.ForeignKey(Measurement,on_delete=models.CASCADE)
    measurement_value=models.IntegerField()
    project_work_status=models.ForeignKey(ProjectWorkStatus,on_delete=models.CASCADE)
    project_financial_status=models.ForeignKey(FinancialStatus,on_delete=models.CASCADE)
    project_remark=models.ManyToManyField(ProjectRemark)

class ProjectImplementationsMedia(models.Model):
    Quarter = (
      ('First', 'First'),
      ('second', 'Second'),
      ('Third', 'Third'),
      ('Forth', 'Forth')
   )
    project=models.ForeignKey(ProjectImplementations, on_delete=models.CASCADE)
    gallery=models.ImageField(upload_to='project_implementations_image',null=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    quarter=models.CharField(max_length=30,choices=Quarter)
    video_file = models.FileField(upload_to='videos/', null=True, )
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)   
    is_active=models.BooleanField(default=True)

