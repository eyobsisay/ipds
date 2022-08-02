from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .project_appraisal import ProjectAppraisal

# result types for evaluations
class Result(models.Model):
    result_name=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.result_name
# project evaluation result 
class ProjectAppraisalEvaluation(models.Model):
    project_appraisal=models.ForeignKey(ProjectAppraisal,on_delete=models.CASCADE)
    arrival_date_of_project_appraisal_to_pds=models.DateTimeField()
    appraisal_result=models.ForeignKey(Result,on_delete=models.CASCADE)
    reason=models.TextField()
    date_of_appraisal_result_sent=models.DateTimeField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

class projectImplementationAndPlan(models.Model):
    project_appraisal=models.ForeignKey(ProjectAppraisal,on_delete=models.CASCADE)    
    arrival_date_of_plane_for_evaluation_pdm=models.DateTimeField()
    evaluation_result=models.ForeignKey(Result,on_delete=models.CASCADE)
    reason=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)