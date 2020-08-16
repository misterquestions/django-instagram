from django.http import HttpResponse, HttpResponseBadRequest
from datetime import datetime
import json

def hello_world(request):
    """Shows a hello world message and a date."""
    date = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello, world! Currently is {date}'.format(date=str(date)))

def sort_numbers(request):
    """"
    Receives a comma-separated param and returns the sorted list of numbers,
    then answers a json object with a sorted list of this numbers
    """
    numbers_to_order = request.GET.get('numbers')

    if numbers_to_order is None:
        return HttpResponseBadRequest('Invalid params supplied')

    ordered_numbers = [int(x) for x in numbers_to_order.split(',')]
    ordered_numbers.sort()
    json_response = {
        'code': 0,
        'status': 'OK',
        'data': {
            'input': numbers_to_order,
            'sorted': ordered_numbers,
        }
    }

    return HttpResponse(json.dumps(json_response), content_type='application/json')

def say_hi(request, name, age):
    """Displays a welcome message or tells the user that is not allowed to use our site"""
    if age < 12:
        message = f'Sorry {name}, you\'re not allowed to use our site'
    else:
        message = f'Hello, {name}! Welcome to Platzigram.'

    return HttpResponse(message)