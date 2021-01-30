from django.shortcuts import render
from .models import Fakedata
from django.http.response import HttpResponse
import faker
fake = faker.Faker()
# Create your views here.
def inserting_data(request):
    for i in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        job = fake.random_element(elements=('Manager','TL','HR','SoftEng','Trainer','Salesman'))
        salary = fake.random_element(elements=(20000,30000,40000,50000,60000,70000))
        city = fake.random_element(elements=('Delhi','Mumbai','Bang','Pune','Hyd','Chennai'))
        dob = fake.date_time()
        address = fake.address()

        data =Fakedata(
            first_name=first_name,
            last_name=last_name,
            email=email,
            job=job,
            salary=salary,
            city=city,
            dob=dob,
            address=address

        )
        data.save()
    return HttpResponse("Data Saved")

# from django.db.models import Q
# def fetching_data(request):
#     total_data = Fakedata.objects.all()
#     filtered_total_data = len(total_data)
#
#     data = Fakedata.objects.all()
#     filtered_data = len(data)
#     return render(request,'fakerfile.html',{'data':data,'filtered_data':filtered_data,'filtered_total_data':filtered_total_data})

def fetching_data(request):
    if request.method =="POST":
        all_data = Fakedata.objects.all()
        final_data =len(all_data)
        job1 = request.POST.get('job')
        data = Fakedata.objects.filter(job=job1)
        filtered_data = len(data)
        return render(request,'fakerfile.html',{'data':data,'final_data':final_data,'filtered_data':filtered_data})

    else:
        data = Fakedata.objects.all()
        return render(request,'fakerfile.html',{'data':data})