from rest_framework import viewsets
from .models import Rule, RuleEvaluation, Comnbiner
from .serializers import RuleSerializer, RuleEvaluationSerializer, CombineRuleSerializer

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class CombineRuleViewSet(viewsets.ModelViewSet):
    queryset = Comnbiner.objects.all()
    serializer_class = CombineRuleSerializer

class RuleEvaluationViewSet(viewsets.ModelViewSet):
    queryset = RuleEvaluation.objects.all()
    serializer_class = RuleEvaluationSerializer
