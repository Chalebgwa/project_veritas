from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BusinessIdea, BusinessPlan, LocationRecommendation, DomainSuggestion, MarketAnalysis
import random


def home(request):
    """Home page view"""
    recent_plans = BusinessIdea.objects.all()[:6]
    context = {
        'recent_plans': recent_plans,
    }
    return render(request, 'business_planner/home.html', context)


def create_business_idea(request):
    """View to create a new business idea"""
    if request.method == 'POST':
        business_name = request.POST.get('business_name')
        business_description = request.POST.get('business_description')
        industry = request.POST.get('industry')
        target_market = request.POST.get('target_market')
        initial_investment = request.POST.get('initial_investment')

        business_idea = BusinessIdea.objects.create(
            user=request.user if request.user.is_authenticated else None,
            business_name=business_name,
            business_description=business_description,
            industry=industry,
            target_market=target_market,
            initial_investment=initial_investment if initial_investment else None
        )

        # Generate business plan
        generate_business_plan(business_idea)
        
        # Generate market analysis
        generate_market_analysis(business_idea)
        
        # Generate location recommendations
        generate_location_recommendations(business_idea)
        
        # Generate domain suggestions
        generate_domain_suggestions(business_idea)

        return redirect('business_plan_detail', pk=business_idea.pk)

    return render(request, 'business_planner/create_idea.html')


def generate_business_plan(business_idea):
    """Generate a business plan for the given business idea"""
    # This is a simplified version. In production, you would use AI/ML models
    success_probability = round(random.uniform(45, 85), 2)
    
    BusinessPlan.objects.create(
        business_idea=business_idea,
        executive_summary=f"This business plan outlines a comprehensive strategy for {business_idea.business_name}, "
                         f"a {business_idea.industry} venture targeting {business_idea.target_market}. "
                         f"The business aims to provide innovative solutions in the {business_idea.industry} sector.",
        market_analysis=f"The {business_idea.industry} market shows promising growth potential. "
                       f"Our target market of {business_idea.target_market} represents a significant opportunity "
                       f"with growing demand for quality services and products.",
        organization_structure="The organization will be structured with a clear hierarchy including executive leadership, "
                              "operational management, and support staff to ensure efficient operations.",
        products_services=f"{business_idea.business_description}",
        marketing_strategy="Our marketing strategy will leverage digital channels, social media, and traditional advertising "
                          "to reach our target audience. We will focus on building brand awareness and customer loyalty.",
        financial_projections="Based on market analysis and industry benchmarks, we project steady revenue growth "
                             "over the first 3-5 years with break-even expected within 18-24 months.",
        success_probability=success_probability
    )


def generate_market_analysis(business_idea):
    """Generate market analysis for the business idea"""
    competition_levels = ['low', 'medium', 'high']
    
    MarketAnalysis.objects.create(
        business_idea=business_idea,
        market_size=f"${random.randint(10, 500)} million",
        growth_rate=round(random.uniform(3.5, 15.5), 2),
        competition_level=random.choice(competition_levels),
        target_demographics=f"The primary target demographic for {business_idea.business_name} includes "
                           f"{business_idea.target_market} with varying income levels and interests.",
        market_trends=f"Current trends in the {business_idea.industry} industry show increasing demand for "
                     "innovation, sustainability, and customer-centric solutions.",
        opportunities="Key opportunities include untapped market segments, technological advancements, "
                     "and evolving customer preferences.",
        threats="Potential threats include market competition, economic downturns, and regulatory changes."
    )


def generate_location_recommendations(business_idea):
    """Generate location recommendations for the business"""
    locations = [
        {'city': 'New York', 'state': 'NY', 'country': 'USA', 'population': 8000000},
        {'city': 'Los Angeles', 'state': 'CA', 'country': 'USA', 'population': 4000000},
        {'city': 'Chicago', 'state': 'IL', 'country': 'USA', 'population': 2700000},
        {'city': 'Austin', 'state': 'TX', 'country': 'USA', 'population': 1000000},
        {'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'population': 900000},
    ]
    
    for location in locations[:3]:
        score = round(random.uniform(65, 95), 2)
        LocationRecommendation.objects.create(
            business_idea=business_idea,
            city=location['city'],
            state=location['state'],
            country=location['country'],
            score=score,
            reasoning=f"{location['city']} offers excellent market potential for {business_idea.industry} "
                     f"businesses with strong demographics and infrastructure.",
            population=location['population'],
            market_size=f"${random.randint(5, 50)} million"
        )


def generate_domain_suggestions(business_idea):
    """Generate domain name suggestions"""
    name_parts = business_idea.business_name.lower().replace(' ', '')
    suggestions = [
        f"{name_parts}.com",
        f"{name_parts}hq.com",
        f"get{name_parts}.com",
        f"{name_parts}online.com",
        f"{name_parts}pro.com",
    ]
    
    for domain in suggestions[:5]:
        # In production, you would check actual availability
        is_available = random.choice([True, False])
        DomainSuggestion.objects.create(
            business_idea=business_idea,
            domain_name=domain,
            is_available=is_available
        )


def business_plan_detail(request, pk):
    """View to display business plan details"""
    business_idea = get_object_or_404(BusinessIdea, pk=pk)
    
    try:
        business_plan = business_idea.business_plan
    except BusinessPlan.DoesNotExist:
        business_plan = None
    
    try:
        market_analysis = business_idea.market_analysis
    except MarketAnalysis.DoesNotExist:
        market_analysis = None
    
    locations = business_idea.locations.all()
    domains = business_idea.domains.all()
    
    context = {
        'business_idea': business_idea,
        'business_plan': business_plan,
        'market_analysis': market_analysis,
        'locations': locations,
        'domains': domains,
    }
    return render(request, 'business_planner/plan_detail.html', context)


class BusinessIdeaListView(ListView):
    """List all business ideas"""
    model = BusinessIdea
    template_name = 'business_planner/idea_list.html'
    context_object_name = 'business_ideas'
    paginate_by = 10

