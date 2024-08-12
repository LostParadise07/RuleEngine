from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rule
from .serializers import RuleSerializer
from .services import create_rule, combine_rules, evaluate_rule

class CreateRuleView(APIView):
    def post(self, request):
        rule_string = request.data.get('rule_string')
        name = request.data.get('name')
        if not rule_string or not name:
            return Response({"error": "Missing rule_string or name"}, status=status.HTTP_400_BAD_REQUEST)

        ast_root = create_rule(rule_string)
        rule = Rule.objects.create(name=name, description=request.data.get('description', ''), ast=ast_root)
        return Response(RuleSerializer(rule).data, status=status.HTTP_201_CREATED)

class CombineRulesView(APIView):
    def post(self, request):
        rule_strings = request.data.get('rules')
        if not isinstance(rule_strings, list) or not all(isinstance(rule, str) for rule in rule_strings):
            return Response({"error": "Invalid rules format"}, status=status.HTTP_400_BAD_REQUEST)

        combined_ast = combine_rules(rule_strings)
        return Response({'combined_ast': combined_ast}, status=status.HTTP_200_OK)

class EvaluateRuleView(APIView):
    def post(self, request):
        ast_json = request.data.get('ast_json')
        data = request.data.get('data')
        if not ast_json or not isinstance(data, dict):
            return Response({"error": "Invalid input data"}, status=status.HTTP_400_BAD_REQUEST)

        result = evaluate_rule(ast_json, data)
        return Response({'result': result}, status=status.HTTP_200_OK)
