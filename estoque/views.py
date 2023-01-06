from django.http import JsonResponse

# from django.shortcuts import render


def api(request):
    return JsonResponse({'data': 1})
