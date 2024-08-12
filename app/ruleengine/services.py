from typing import Dict, Any, List, Union

class ASTNode:
    def __init__(self, type: str, left: 'ASTNode' = None, right: 'ASTNode' = None, value: Any = None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

def create_rule(rule_string: str) -> Dict:
    # Convert the rule_string into an ASTNode in dictionary form
    return parse_rule(rule_string)

def combine_rules(rules: List[str]) -> Dict:
    if not rules:
        return None
    
    # Create an initial AST from the first rule
    combined_ast = create_rule(rules[0])
    
    # Combine each subsequent rule with the current combined AST using AND operator
    for rule in rules[1:]:
        rule_ast = create_rule(rule)
        combined_ast = combine_ast(combined_ast, rule_ast)
    
    return combined_ast

def evaluate_rule(ast_node: Dict, data: Dict[str, Any]) -> bool:
    if ast_node['type'] == 'operand':
        return evaluate_operand(ast_node, data)
    elif ast_node['type'] == 'operator':
        return evaluate_operator(ast_node, data)

def parse_rule(rule_string: str) -> Dict:
    # Basic parsing logic for demonstration
    tokens = rule_string.split()
    if len(tokens) == 3:
        return {
            'type': 'operand',
            'value': rule_string
        }
    return {}

def combine_ast(ast1: Dict, ast2: Dict) -> Dict:
    # Combine two AST nodes using an AND operator
    combined_node = {
        'type': 'operator',
        'value': 'AND',
        'left': ast1,
        'right': ast2
    }
    return combined_node

def evaluate_operand(node: Dict, data: Dict[str, Any]) -> bool:
    # Simple operand evaluation
    operand = node['value']
    if '>' in operand:
        field, value = operand.split('>')
        return data.get(field.strip()) > int(value.strip())
    elif '=' in operand:
        field, value = operand.split('=')
        return data.get(field.strip()) == value.strip().strip("'")
    return False

def evaluate_operator(node: Dict, data: Dict[str, Any]) -> bool:
    left_result = evaluate_rule(node['left'], data)
    right_result = evaluate_rule(node['right'], data)
    if node['value'] == 'AND':
        return left_result and right_result
    elif node['value'] == 'OR':
        return left_result or right_result
    return False
