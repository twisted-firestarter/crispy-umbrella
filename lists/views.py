from django.shortcuts import render


def home_page(request):
    context = {
        'new_item_text': request.POST.get('item_text', ''),
    }
    return render(request, 'home.html', context=context)
