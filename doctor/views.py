from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Doctor
from .forms import DoctorForm
from .serializers import DoctorSerializer
from django.http import Http404



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

@csrf_exempt   
def doctor_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def doctor_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DoctorSerializer(doctor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        doctor.delete()
        return HttpResponse(status=204)












class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
      content = JSONRenderer().render(data)
      kwargs['content_type'] = 'application/json'
      super(JSONResponse, self).__init__(content, **kwargs)