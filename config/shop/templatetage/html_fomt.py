from django import template

def currency_dola(template_name, context):
    return f"{value:.2f} $"

register = template.Library()

register.filter('currency_dola', currency_dola)