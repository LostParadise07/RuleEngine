from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RuleViewSet, RuleEvaluationViewSet,CombineRuleViewSet
from .api_views import CreateRuleView, CombineRulesView, EvaluateRuleView

router = DefaultRouter()
router.register(r'rules', RuleViewSet)
router.register(r'combine_rules', CombineRuleViewSet)
router.register(r'evaluations', RuleEvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_rule/', CreateRuleView.as_view(), name='create_rule'),
    path('combine_rules/', CombineRulesView.as_view(), name='combine_rules'),
    path('evaluate_rule/', EvaluateRuleView.as_view(), name='evaluate_rule'),
]