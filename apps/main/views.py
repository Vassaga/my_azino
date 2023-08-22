"""MAIN APP"""

from django.shortcuts import render

def main_page(request):
    return render(
        template_name='new_main.html',
        request=request
    )