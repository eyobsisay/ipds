from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
# 
# name of project supervising sectors
class ProjectSupervisingSector(models.Model):
    sector_name=models.CharField(max_length=200,null=False,blank=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.sector_name
# name and address of project owner 
class ProjectOwner(models.Model):
    owner_name=models.CharField(max_length=200,null=False,blank=False)
    ministry_phone_number=PhoneNumberField()
    main_department_phone_number=PhoneNumberField()
    email=models.EmailField()
    website=models.URLField()
    owner_office_place=models.CharField(max_length=300)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.owner_name
    # direct and indirect beneficiaries the project  
class ProjectIntendedBeneficiaries(models.Model):
    direct_beneficiaries=models.TextField(max_length=500)
    indirect_beneficiaries=models.TextField(max_length=500)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.direct_beneficiaries + " " + self.indirect_beneficiaries
# all region in ethiopia
class Region(models.Model):
    name=models.CharField(max_length=20)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
# all zones find in region ethiopia
class Zone(models.Model):
    region=models.ForeignKey(Region, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)    
    def __str__(self):
        return self.name
# all woreda found in zone 
class Woreda(models.Model):
    zone=models.ForeignKey(Zone, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)  
    def __str__(self):
        return self.name
# project site address    
class ProjectSite(models.Model):
    region=region=models.ForeignKey(Region, on_delete=models.CASCADE)
    zone=models.ForeignKey(Zone, on_delete=models.CASCADE)
    woreda=models.ForeignKey(Woreda, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
# fund type for project    
class Domestic(models.Model):
    chooses = (
      ('Treasury', 'Treasury'),
      ('Bank Loan', 'Bank Loan'),
   )
    name=models.CharField(max_length=50,choices=chooses)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
# fund type for project 
class Abroad(models.Model):
    chooses = (
      ('Loan' ,'Loan'),
      ('Grant Aid', 'Grant Aid'),
   )
    name=models.CharField(max_length=50,choices=chooses)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    # fund type for project 
class loaderOrAiders(models.Model):
    name=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
# fund type for project     
class ExternalLoan(models.Model):
    loaner_name=models.ForeignKey(loaderOrAiders, on_delete=models.CASCADE)
    other=models.CharField(max_length=100,blank=True,null=True)
    loan_amount_etb=models.IntegerField()
    loan_amount_usd=models.IntegerField()
    loan_duration=models.DateField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
# fund type for project     
class ExternalAid(models.Model):
    aider_name=models.ForeignKey(loaderOrAiders, on_delete=models.CASCADE)
    other=models.CharField(max_length=100,blank=True,null=True)
    aid_amount_etb=models.IntegerField()
    aid_amount_usd=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
# fund type for project     
class Jointly(models.Model):
    name_of_country=models.ForeignKey(loaderOrAiders, on_delete=models.CASCADE)
    other=models.CharField(max_length=100,blank=True,null=True)
    inland_share_etb=models.IntegerField()
    abroad_share_etb=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)   
     
# project finance source detail information     
class ProjectSourceDetail(models.Model):
    domestic=models.ForeignKey(Domestic, on_delete=models.CASCADE)
    abroad=models.ForeignKey(Abroad, on_delete=models.CASCADE)
    external_loan=models.ForeignKey(ExternalLoan, on_delete=models.CASCADE)
    external_aid=models.ForeignKey(ExternalAid, on_delete=models.CASCADE)
    jointly=models.ForeignKey(Jointly, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
# project fiance source type choose and amount  
class ProjectFinance(models.Model):
    source = (
      ('Domestic', 'Domestic'),
      ('Abroad', 'Abroad'),
      ('Domestic & Abroad', 'Domestic & Abroad')
   )
    investment_cost_etb=models.IntegerField()
    investment_cost_usd=models.IntegerField()
    project_finance_source=models.CharField(max_length=30,choices=source)
    project_source_detail=models.ForeignKey(ProjectSourceDetail, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def finance_type(self):
        if self.project_finance_source == 'Domestic':
            return 'Domestic'
        elif self.project_finance_source == 'Abroad': 
            return 'Abroad'
        elif self.project_finance_source == 'Domestic & Abroad':
            return 'Domestic & Abroad'
        else:
            return 'none'    

# project appraisal and all necessary information for project    
# TODO:project site must to be many to many relation to accept adjacent Region

class ProjectAppraisal(models.Model):
    region = (
      ('one region', 'one region'),
      ('adjacent region', 'adjacent region')
   )
    project_name=models.CharField(max_length=200,blank=False,null=False)
    project_supervising_sector=models.ForeignKey(ProjectSupervisingSector,related_name='project_evaluation_sector', on_delete=models.CASCADE)
    project_owner=models.ForeignKey(ProjectOwner,related_name='project_owner', on_delete=models.CASCADE)
    project_outcome=models.TextField()
    project_intended_beneficiaries=models.ForeignKey(ProjectIntendedBeneficiaries,related_name='project_intended_beneficiaries',on_delete=models.CASCADE)
    project_regions=models.CharField(max_length=400, default='active', blank=True, choices=region)
    project_site=models.ForeignKey(ProjectSite,related_name='project_site', on_delete=models.CASCADE)
    project_finance=models.ForeignKey(ProjectFinance,related_name='project_finance', on_delete=models.CASCADE)
    project_duration=models.DateField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.project_name

class ProjectAppraisalMedia(models.Model):
    Quarter = (
      ('First', 'First'),
      ('second', 'Second'),
      ('Third', 'Third'),
      ('Forth', 'Forth')
   )
    project=models.ForeignKey(ProjectAppraisal, on_delete=models.CASCADE)
    gallery=models.ImageField(upload_to='project_appraisal_image',null=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    video_file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    quarter=models.CharField(max_length=30,choices=Quarter)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)


