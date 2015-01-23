from django import template

register = template.Library()

@register.filter(name='find_all')
def find_all(value, arg):
	return value.objects.filter(thread=arg)