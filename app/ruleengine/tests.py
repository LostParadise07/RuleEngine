from django.test import TestCase
from .services import create_rule, combine_rules, evaluate_rule

class RuleEngineTests(TestCase):
    def test_create_rule(self):
        rule_string = "age > 30"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)

    def test_combine_rules(self):
        rules = ["age > 30", "salary > 50000"]
        combined_ast = combine_rules(rules)
        self.assertIsNotNone(combined_ast)

    def test_evaluate_rule(self):
        ast_json = {
            'type': 'operator',
            'value': 'AND',
            'left': {'type': 'operand', 'value': 'age > 30'},
            'right': {'type': 'operand', 'value': 'salary > 50000'}
        }
        data = {'age': 35, 'salary': 60000}
        result = evaluate_rule(ast_json, data)
        self.assertTrue(result)
