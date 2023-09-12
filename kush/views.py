from django.shortcuts import render
from django.http import JsonResponse
# import datetime
from .models import Person

# def api(request):
#     # Get query parameters
#     slack_name = request.GET.get('slack_name')
#     track = request.GET.get('track')

#     # Get current day and UTC time
#     current_day = datetime.datetime.now().strftime("%A")
#     utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

#     # Validate UTC time (within +/- 2 seconds)
#     utc_time_datetime = datetime.datetime.strptime(utc_time, "%Y-%m-%dT%H:%M:%SZ")
#     current_utc_time = datetime.datetime.utcnow()

#     if abs((current_utc_time - utc_time_datetime).total_seconds()) > 2:
#         return JsonResponse({"error": "Invalid UTC time"}, status=400)

    # Construct GitHub URLs
    # github_file_url = "https://github.com/priest-tech/stage_one/blob/main/kush/views.py"
    # github_repo_url = "https://github.com/priest-tech/stage_one"

    # # Create JSON response
    # response_data = {
    #     "slack_name": slack_name,
    #     "current_day": current_day,
    #     "utc_time": utc_time,
    #     "track": track,
    #     "github_file_url": github_file_url,
    #     "github_repo_url": github_repo_url,
    #     "status_code": 200
    # }

    # return JsonResponse(response_data)
    #CREATE
from django.shortcuts import render
from django.http import JsonResponse
# import datetime
from .models import Person

def create_person_form(request):
    return render(request, 'kush/create_person.html', {
        'url': '/create/'
    })

# CREATE
def create_person(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        if not name:
            return JsonResponse({"error": "Name is required"}, status=400)
        
        person = Person(name=name) #creating a person instance

        try:
            person.save()
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)    
        
        #Return a JSON response with the new person's details

        response_data = {
            "id": person.id, #auto-generated primary Key
            "name": person.name,
            "email":person.email,
            "age":person.age
        }

        return JsonResponse(response_data, status=201) #a success response created with 201(Created)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405) #Error for unsupported HTTP methods

# READ
def get_person(request):

    try:
        # Retrieve the person by name or user_id from the database
        name = request.GET.get('name')
        user_id = request.GET.get('id')

        if name:
            persons = Person.objects.filter(name=name)
        elif user_id:
            persons = [Person.objects.get(id=user_id)]
        else:
            return JsonResponse({"error": "Name or ID parameter is required"}, status=400)

        # Create a list of JSON responses for each person found
        response_data = []

        for person in persons:
            person_data = {
                "id": person.id,
                "name": person.name,
                "email": person.email,
                "age": person.age
            }
            response_data.append(person_data)

        return JsonResponse(response_data, safe=False, status=200)

    except Person.DoesNotExist:
        return JsonResponse({"error": "Person not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

#UPDATE
def update_person(request, user_id):
    try:
        #Retrieve the person user_id from the database
        person =Person.objects.get(id=user_id)    
        #request to update person details
        if request.method == 'POST':
            # Retrieve and validate input data( name, age, email)
            name=request.POST.get('name')
            age=request.POST.get('age')
            email=request.POST.get('email')

            #Update the person's details based on the input data
            if name:
                person.name= name
            if age:
                person.age = age
            if email:
                person.email = email
            #Save the updated person instances to the database
            person.save()

            # Return a JSON response with the updated person's details

            response_data = {
                "id": person.id,
                "name": person.name,
                "email": person.email,
                "age": person.age           
                  }            
            
            return JsonResponse(response_data,status=200)
        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)
    except Person.DoesNotExist:
        return JsonResponse({"error":"Person not found"},status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
#DELETE
def delete_person(request,user_id):
    try:
        # Retrieve the person by user_id
        person = Person.objects.get(id=user_id)
        #Delete the person instance from the database
        person.delete()

        return JsonResponse({"message":"Person deleted successfully"},status=200)
    except Person.DoesNotExist:
        return JsonResponse({"error":"Person not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error":"str(e)"},status=500)    


        
# Create your views here.

