from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from . models import Doctor, Contact,Prescription_pictures,Bloodds
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout , login, authenticate
from . forms import Presform
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/loginuser/")
    else:
        messages.success(request, 'Welcome ')
        return render(request, 'index.html')


def loginuser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
                            auth.login(request, user)
                            return redirect("/")

        else:
            return redirect("/loginuser/")

    else:
          return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect("/loginuser/")


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user=User.objects.create_user(first_name=first_name, last_name=last_name,username=username, email=email, password=password)
        user.save()
        print("created")
        return redirect('/loginuser/')
    else:
        return render(request, 'register.html')




def doctorsearch(request):
    query = request.GET.get('search')
    allD= Doctor.objects.filter(Q(registration_number__icontains=query))
    params = {'allD': allD}
    if len(query) == 0 and query != len(allD):
        return render(request, 'doctor.html')
    else:
        return render(request, 'doctor_search.html', params)


def contact(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        msg = request.POST.get('msg', '')
        if len(first_name)<4 or len(last_name)<2 or len(email)<4 or len(subject)<4 or len(msg)<4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            contact = Contact(first_name=first_name, last_name=last_name, email=email, subject=subject, msg=msg)
            contact.save()
            messages.success(request, 'Your message has been sent.')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def doctor(request):
    return render(request, 'doctor.html')


def medicine(request):
    return render(request, 'medicine.html')


def p(request):
    if request.method == 'POST':
        form = Presform(request.POST, request.FILES)
        if form.is_valid():
            #for saving data without user drop down(which comes from  model)
            data= form.save(commit=False)
            data.user = request.user
            data.save()
            return render(request, 'pres.html', {'form': form})
    else:
        form = Presform()
        return render(request, 'pres.html',{'form': form})

@login_required(login_url='/loginuser/')
def pres_show(request):
       log_user = request.user
       pic = Prescription_pictures.objects.filter(user=log_user)
       params = {'pic': pic}
       return render(request, 'pres_show.html',params)


@login_required(login_url='/loginuser/')
def delete_pres(request, pk):
    if request.method == 'POST':
        pic = Prescription_pictures.objects.get(pk=pk)
        pic.delete()
    return redirect("/")


@login_required(login_url='/loginuser/')
def delete_donner(request, pk):
    if request.method == 'POST':
        dnr = Bloodds.objects.get(pk=pk)
        dnr.delete()
    return redirect("/")


def donner(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        bloodgroup = request.POST.get('bloodgroup', '')
        address = request.POST.get('address', '')
        lastdonate = request.POST.get('lastdonate', '')

        doner = Bloodds(name=name, age=age,phone=phone, email=email, bloodgroup=bloodgroup,address=address,lastdonate=lastdonate)
        data = doner
        data.user = request.user
        data.save()
    return render(request, 'donner.html')

@login_required(login_url='/loginuser/')
def donnershow(request):
    log_user = request.user
    dnr = Bloodds.objects.filter(user=log_user)
    params = {'dnr': dnr}
    return render(request, 'donner_show.html',params)


