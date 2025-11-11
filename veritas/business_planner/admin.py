from django.contrib import admin
from .models import BusinessIdea, BusinessPlan, LocationRecommendation, DomainSuggestion, MarketAnalysis


@admin.register(BusinessIdea)
class BusinessIdeaAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'industry', 'created_at', 'user']
    list_filter = ['industry', 'created_at']
    search_fields = ['business_name', 'business_description']
    date_hierarchy = 'created_at'


@admin.register(BusinessPlan)
class BusinessPlanAdmin(admin.ModelAdmin):
    list_display = ['business_idea', 'success_probability', 'created_at']
    list_filter = ['created_at']
    search_fields = ['business_idea__business_name']
    date_hierarchy = 'created_at'


@admin.register(LocationRecommendation)
class LocationRecommendationAdmin(admin.ModelAdmin):
    list_display = ['city', 'state', 'country', 'score', 'business_idea']
    list_filter = ['country', 'state']
    search_fields = ['city', 'business_idea__business_name']


@admin.register(DomainSuggestion)
class DomainSuggestionAdmin(admin.ModelAdmin):
    list_display = ['domain_name', 'is_available', 'business_idea', 'checked_at']
    list_filter = ['is_available', 'checked_at']
    search_fields = ['domain_name', 'business_idea__business_name']


@admin.register(MarketAnalysis)
class MarketAnalysisAdmin(admin.ModelAdmin):
    list_display = ['business_idea', 'competition_level', 'growth_rate', 'created_at']
    list_filter = ['competition_level', 'created_at']
    search_fields = ['business_idea__business_name']

