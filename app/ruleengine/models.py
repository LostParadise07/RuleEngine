from django.db import models
from django.db.models import JSONField

class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ast = JSONField()  # Store the AST as JSON

    def __str__(self):
        return self.name

class RuleEvaluation(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    input_data = JSONField()
    result = models.BooleanField()

    def __str__(self):
        return f"Evaluation for {self.rule.name}"


class Comnbiner(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ast = JSONField()  # Store the AST as JSON

    def __str__(self):
        return self.name