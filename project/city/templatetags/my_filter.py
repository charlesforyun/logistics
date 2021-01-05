from django import template

register = template.Library()


@register.filter(name="ge")
def greet(value, word):
    return value + word


@register.filter
def greet_2(value, word):
    return value + word


# register.filter('greet', greet)
# register.filter("gerrt2", greet_2)


