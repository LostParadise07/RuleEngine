from rest_framework import serializers
from .models import Rule, RuleEvaluation

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ['id', 'name', 'description', 'ast']

class RuleEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleEvaluation
        fields = ['id', 'rule', 'input_data', 'result']

class CombineRuleSerializer(serializers.Serializer):
    rules = serializers.ListField(child=serializers.CharField())
