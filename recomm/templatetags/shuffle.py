import random
from django import template
register = template.Library()

@register.filter
def shuffle(arg):
    # print(arg)
    aux = list(arg)[:]
    random.shuffle(aux)
    return aux
