from django.contrib import admin

from . import models


class ConsultantTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'consultant_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'consultant_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class MeasurementAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'measurement_name',
        'desc',
        'si_unit',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'measurement_name',
        'desc',
        'si_unit',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class WorkStatusTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'status_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    list_filter = (
        'created_date',
        'updated_at',
        'is_active',
        'id',
        'status_name',
        'created_date',
        'updated_at',
        'is_active',
    )
    date_hierarchy = 'updated_at'


class QuarterWorkPlaneAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
    list_filter = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )


class ProjectWorkStatusAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'work_status',
        'current_budget_year',
        'pre_b_year_work_perf_in_percent',
        'physical_work_plan_year',
        'project_work_pane_in_four_quarter',
        'project_work_performance_quarter',
        'project_performance_to_plan_ratio',
        'YTD_physical_work_plan',
        'YTD_physical_work_performance',
        'YTD_performance_to_plan_ratio',
    )
    list_filter = (
        'work_status',
        'current_budget_year',
        'project_work_pane_in_four_quarter',
        'id',
        'work_status',
        'current_budget_year',
        'pre_b_year_work_perf_in_percent',
        'physical_work_plan_year',
        'project_work_pane_in_four_quarter',
        'project_work_performance_quarter',
        'project_performance_to_plan_ratio',
        'YTD_physical_work_plan',
        'YTD_physical_work_performance',
        'YTD_performance_to_plan_ratio',
    )


class QuarterFinancialPlanAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
    list_filter = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )


class QuarterFinancialPerformanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
    list_filter = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )


class QuarterFinancialRatioAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
    list_filter = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
class QuarterWorkPerformanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
    list_filter = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
class QuarterWorkPerformanceToPlanRatioAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )
    list_filter = (
        'id',
        'first_quarter',
        'second_quarter',
        'third_quarter',
        'fourth_quarter',
    )        


class FinancialStatusAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'pre_b_year_financial_performance_birr',
        'budget_financial_plan',
        'quarter_plan',
        'quarter_financial_plan',
        'quarter_financial_performance',
        'quarter_financial_ratio',
        'YTD_financial_work_plan',
        'YTD_financial_work_performance',
        'YTD_financial_performance_to_plan_ratio',
    )
    list_filter = (
        'quarter_financial_plan',
        'quarter_financial_performance',
        'quarter_financial_ratio',
        'id',
        'pre_b_year_financial_performance_birr',
        'budget_financial_plan',
        'quarter_plan',
        'quarter_financial_plan',
        'quarter_financial_performance',
        'quarter_financial_ratio',
        'YTD_financial_work_plan',
        'YTD_financial_work_performance',
        'YTD_financial_performance_to_plan_ratio',
    )


class ProjectRemarkAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'budget_year_obstacle',
        'project_total_limitation',
        'project_comment',
        'project_file',
    )
    list_filter = (
        'id',
        'budget_year_obstacle',
        'project_total_limitation',
        'project_comment',
        'project_file',
    )


class ProjectImplementationsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project',
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
    )
    list_filter = (
        'project',
        'project_starting_date',
        'project_ending_date',
        'project_consultant_type',
        'project_contractor_type',
        'project_measurement',
        'project_work_status',
        'project_financial_status',
        'id',
        'project',
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
    )
    raw_id_fields = ('project_remark',)
class ProjectImplementationsMediaAdmin(admin.ModelAdmin):

    
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

_register(models.ProjectImplementationsMedia, ProjectImplementationsMediaAdmin)

_register(models.ConsultantType, ConsultantTypeAdmin)
_register(models.Measurement, MeasurementAdmin)
_register(models.WorkStatusType, WorkStatusTypeAdmin)
_register(models.QuarterWorkPlane, QuarterWorkPlaneAdmin)
_register(models.QuarterWorkPerformanceToPlanRatio, QuarterWorkPerformanceToPlanRatioAdmin)

_register(models.ProjectWorkStatus, ProjectWorkStatusAdmin)
_register(models.QuarterFinancialPlan, QuarterFinancialPlanAdmin)
_register(models.QuarterFinancialPerformance,QuarterFinancialPerformanceAdmin)
_register(models.QuarterWorkPerformance, QuarterWorkPerformanceAdmin)    
_register(models.QuarterFinancialRatio, QuarterFinancialRatioAdmin)
_register(models.FinancialStatus, FinancialStatusAdmin)
_register(models.ProjectRemark, ProjectRemarkAdmin)
_register(models.ProjectImplementations, ProjectImplementationsAdmin)
