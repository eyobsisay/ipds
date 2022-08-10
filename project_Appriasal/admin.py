from django.contrib import admin

from . import models


class ProjectSupervisingSectorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'sector_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'sector_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ProjectOwnerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'owner_name',
        'ministry_phone_number',
        'main_department_phone_number',
        'email',
        'website',
        'owner_office_place',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'owner_name',
        'ministry_phone_number',
        'main_department_phone_number',
        'email',
        'website',
        'owner_office_place',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ProjectIntendedBeneficiariesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'direct_beneficiaries',
        'indirect_beneficiaries',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'direct_beneficiaries',
        'indirect_beneficiaries',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class RegionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_date', 'updated_at', 'is_active')
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


class ZoneAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'region',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'region',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'region',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


class WoredaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'zone',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'zone',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'zone',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


class ProjectSiteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'region',
        'zone',
        'woreda',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'region',
        'zone',
        'woreda',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'region',
        'zone',
        'woreda',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class DomesticAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_date', 'updated_at', 'is_active')
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


class AbroadAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_date', 'updated_at', 'is_active')
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


class loaderOrAidersAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_date', 'updated_at', 'is_active')
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'name',
        'created_date',
        'updated_at',
        'is_active',
    )
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


class ExternalLoanAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'loaner_name',
        'other',
        'loan_amount_etb',
        'loan_amount_usd',
        'loan_duration',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'loaner_name',
        'loan_duration',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'loaner_name',
        'other',
        'loan_amount_etb',
        'loan_amount_usd',
        'loan_duration',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ExternalAidAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'aider_name',
        'other',
        'aid_amount_etb',
        'aid_amount_usd',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'aider_name',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'aider_name',
        'other',
        'aid_amount_etb',
        'aid_amount_usd',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class JointlyAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name_of_country',
        'other',
        'inland_share_etb',
        'abroad_share_etb',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'name_of_country',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'name_of_country',
        'other',
        'inland_share_etb',
        'abroad_share_etb',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ProjectSourceDetailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'domestic',
        'abroad',
        'external_loan',
        'external_aid',
        'jointly',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'domestic',
        'abroad',
        'external_loan',
        'external_aid',
        'jointly',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'domestic',
        'abroad',
        'external_loan',
        'external_aid',
        'jointly',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ProjectFinanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'investment_cost_etb',
        'investment_cost_usd',
        'project_finance_source',
        'project_source_detail',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'project_source_detail',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'investment_cost_etb',
        'investment_cost_usd',
        'project_finance_source',
        'project_source_detail',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ProjectAppraisalAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project_name',
        'project_supervising_sector',
        'project_outcome',
        'project_intended_beneficiaries',
        'project_regions',
        'project_site',
        'project_finance',
        'project_duration',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'project_supervising_sector',
        'project_intended_beneficiaries',
        'project_site',
        'project_finance',
        'project_duration',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'project_name',
        'project_supervising_sector',
        'project_outcome',
        'project_intended_beneficiaries',
        'project_regions',
        'project_site',
        'project_finance',
        'project_duration',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ResultAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'result_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'result_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class ProjectAppraisalEvaluationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project_appraisal',
        'arrival_date_of_project_appraisal_to_pds',
        'appraisal_result',
        'reason',
        'date_of_appraisal_result_sent',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'project_appraisal',
        'arrival_date_of_project_appraisal_to_pds',
        'appraisal_result',
        'date_of_appraisal_result_sent',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'project_appraisal',
        'arrival_date_of_project_appraisal_to_pds',
        'appraisal_result',
        'reason',
        'date_of_appraisal_result_sent',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class projectImplementationAndPlanAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project_appraisal',
        'arrival_date_of_plane_for_evaluation_pdm',
        'evaluation_result',
        'reason',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'project_appraisal',
        'arrival_date_of_plane_for_evaluation_pdm',
        'evaluation_result',
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'project_appraisal',
        'arrival_date_of_plane_for_evaluation_pdm',
        'evaluation_result',
        'reason',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'
class ProjectAppraisalMediaMediaAdmin(admin.ModelAdmin):

    
    list_display = (
        'id',
        'project',
        'gallery',
        'description',
        'video_file',
        'quarter',
        'created_date',
        'updated_at',
        'is_active',
        
    )

def _register(model, admin_class):
    admin.site.register(model, admin_class)
_register(models.ProjectAppraisalMedia, ProjectAppraisalMediaMediaAdmin)

_register(models.ProjectSupervisingSector, ProjectSupervisingSectorAdmin)
_register(models.ProjectOwner, ProjectOwnerAdmin)
_register(
    models.ProjectIntendedBeneficiaries,
    ProjectIntendedBeneficiariesAdmin)
_register(models.Region, RegionAdmin)
_register(models.Zone, ZoneAdmin)
_register(models.Woreda, WoredaAdmin)
_register(models.ProjectSite, ProjectSiteAdmin)
_register(models.Domestic, DomesticAdmin)
_register(models.Abroad, AbroadAdmin)
_register(models.loaderOrAiders, loaderOrAidersAdmin)
_register(models.ExternalLoan, ExternalLoanAdmin)
_register(models.ExternalAid, ExternalAidAdmin)
_register(models.Jointly, JointlyAdmin)
_register(models.ProjectSourceDetail, ProjectSourceDetailAdmin)
_register(models.ProjectFinance, ProjectFinanceAdmin)
_register(models.ProjectAppraisal, ProjectAppraisalAdmin)
_register(models.Result, ResultAdmin)
_register(models.ProjectAppraisalEvaluation, ProjectAppraisalEvaluationAdmin)
_register(
    models.projectImplementationAndPlan,
    projectImplementationAndPlanAdmin)
