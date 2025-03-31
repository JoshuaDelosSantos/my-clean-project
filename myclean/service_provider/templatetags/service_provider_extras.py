from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Template filter to access dictionary items by key.
    Usage: {{ dictionary|get_item:key }}
    """
    return dictionary.get(key, [])