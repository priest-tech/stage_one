from django.shortcuts import render
from django.http import JsonResponse
import datetime

def api(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Get current day and UTC time
    current_day = datetime.datetime.now().strftime("%A")
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Validate UTC time (within +/- 2 seconds)
    utc_time_datetime = datetime.datetime.strptime(utc_time, "%Y-%m-%dT%H:%M:%SZ")
    current_utc_time = datetime.datetime.utcnow()

    if abs((current_utc_time - utc_time_datetime).total_seconds()) > 2:
        return JsonResponse({"error": "Invalid UTC time"}, status=400)

    # Construct GitHub URLs
    github_file_url = "https://github.com/priest-tech/Zuri/blob/stage_one/myproject/myapp/views.py"
    github_repo_url = "https://github.com/priest-tech/Zuri"

    # Create JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)


# Create your views here.
