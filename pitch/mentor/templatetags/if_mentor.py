from django import template



register = template.Library()


def if_mentor():
    u = context['request'].user
    if u == "bivu":
        return True
    else:
        return False
