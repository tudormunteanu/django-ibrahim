from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Doctor
from .forms import DoctorForm
from .serializers import DoctorSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




def create_user(request):

	if request.method == 'POST':
		form = DoctorForm(request.POST)
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect('thanks/')
	else:
		form = DoctorForm()

	context = { 
	'form': form
	}

	return render(request, 'doctor/signup.html', context)



def signup(request):

	if request.method == 'POST':
		form = DoctorForm(request.POST)
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect('thanks/')
	else:
		form = DoctorForm()

	context = { 
	'form': form
	}

	return render(request, 'doctor/signup.html', context)


def signin(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            return render(request, 'doctor/signup.html', context)

    else:
    	pass
        # Return an 'invalid login' error message.



def index(request):
    #return HttpResponse("Hello, world. You're at the doctor index.")
    #return render(request, 'doctor/index.html')
	doctor_list = Doctor.objects.order_by('last_name')
	context = {
	'doctor_list': doctor_list,
		}

	return render(request, 'doctor/index.html', context)


def doctor(request, doctor_id):

	try:
		doctor = Doctor.objects.get(pk=doctor_id)
	except Doctor.DoesNotExist:
		raise Http404("Doctor does not exist")
	return render(request, 'doctor/doctor.html', {'doctor': doctor})


 # API starts here 

class JSONResponse(HttpResponse): #(what is this for????) <----
     """
     An HttpResponse that renders its content into JSON.
     """
     def __init__(self, data, **kwargs):
         content = JSONRenderer().render(data)
         kwargs['content_type'] = 'application/json'
         super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt   
@api_view(['GET', 'POST'])
def doctor_list(request):
    """
    List all doctors
    """
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JsonParser().parse(request)
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def doctor_detail(request, pk):

    """
    Retrieve information on one doctor
    """
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JsonParser().parse(request)
        serializer = DoctorSerializer(doctor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        doctor.delete()
        return HttpResponse(status=204)










