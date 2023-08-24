from django import template
import os
register = template.Library()

@register.filter(name='get_range') 
def get_range(number):
    return range(int(number))

@register.filter(name='get_from_dict') 
def get_from_dict(my_dict, i):
    return my_dict.get(i, None)

@register.filter(name='modulus')
def modulus(value, arg):
    return value % arg
