from django.http import JsonResponse
import requests

def get_openf1_data(request):
    # Make a GET request to the OpenF1 API
    response = requests.get('https://api.openf1.org/v1/drivers?driver_number=1&session_key=9158')

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON data from the OpenF1 API
        return JsonResponse(response.json())
    else:
        # Return an error message if the request failed
        return JsonResponse({'error': 'Failed to fetch data from OpenF1 API'}, status=500)
