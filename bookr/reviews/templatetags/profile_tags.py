from django import template
from django.template.defaultfilters import stringfilter

from reviews.models import Review

register = template.Library()


@register.inclusion_tag('book_list.html')
def book_list(username):
    reviews = Review.objects.filter(creator__username__contains=username)
    book_list = [review.book.title for review in reviews]
    return {'book_read': book_list}


@register.filter
def moj_filtr(value, arg):
    return value.split(arg)

@register.filter
@stringfilter
def generic(value,arg):
    pass