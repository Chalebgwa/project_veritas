from django.db import models
from django.contrib.auth.models import User


class BusinessIdea(models.Model):
    """Model to store basic business idea information"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    business_name = models.CharField(max_length=200)
    business_description = models.TextField()
    industry = models.CharField(max_length=100)
    target_market = models.CharField(max_length=200)
    initial_investment = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.business_name


class BusinessPlan(models.Model):
    """Model to store generated business plans"""
    business_idea = models.OneToOneField(BusinessIdea, on_delete=models.CASCADE, related_name='business_plan')
    executive_summary = models.TextField()
    market_analysis = models.TextField()
    organization_structure = models.TextField()
    products_services = models.TextField()
    marketing_strategy = models.TextField()
    financial_projections = models.TextField()
    success_probability = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Business Plan for {self.business_idea.business_name}"


class LocationRecommendation(models.Model):
    """Model to store location recommendations for businesses"""
    business_idea = models.ForeignKey(BusinessIdea, on_delete=models.CASCADE, related_name='locations')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    reasoning = models.TextField()
    population = models.IntegerField(null=True, blank=True)
    market_size = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ['-score']

    def __str__(self):
        return f"{self.city}, {self.state} - Score: {self.score}"


class DomainSuggestion(models.Model):
    """Model to store domain name suggestions"""
    business_idea = models.ForeignKey(BusinessIdea, on_delete=models.CASCADE, related_name='domains')
    domain_name = models.CharField(max_length=200)
    is_available = models.BooleanField(default=False)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain_name


class MarketAnalysis(models.Model):
    """Model to store market analysis data"""
    business_idea = models.OneToOneField(BusinessIdea, on_delete=models.CASCADE, related_name='market_analysis')
    market_size = models.CharField(max_length=200)
    growth_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    competition_level = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])
    target_demographics = models.TextField()
    market_trends = models.TextField()
    opportunities = models.TextField()
    threats = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Market Analysis for {self.business_idea.business_name}"

