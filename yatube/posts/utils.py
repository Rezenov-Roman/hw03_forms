from yatube.settings import NUMBER10
from django.core.paginator import Paginator


def paginator(request, queryset):
    paginator = Paginator(queryset, NUMBER10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return context['page_obj']
