from django.shortcuts import render
#ialngin kebutuhan cek csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
#untuk proteksi page.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import ProjectModel,EventModel,DonateModel,ResponseModel
import json
import logging
from django.http import HttpResponse

from datetime import date,datetime
from django.utils import timezone


#format date agar bisa di dump sebagai json
def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    # else:
    #     raise TypeError


# =========================================================================================
# ===                               Home                                                ===
# =========================================================================================

def home_view(request):
    if request.method == 'GET':
        # coworking = CoWorkingModels.objects.get(pk=coworking_id)
        # return render(request, 'home_yukbelajar.html', context = {
        #     'coworking' : coworking,
        # })
        return render(request, 'index.html')

def tryout_view(request):
    if request.method == 'GET':
        return render(request, 'tryout+counter.html')
def pg_view(request):
    if request.method == 'GET':
        return render(request, 'pg.html')

def get_picture(request):
  pictures = ProjectModel.objects.all()
  result = [picture.as_dict() for picture in pictures]
  as_json= json.dumps(result, default=date_handler, indent=2, ensure_ascii=False)
  return HttpResponse (as_json, content_type="application/json")

def get_event(request):
  events = EventModel.objects.all()
  result = [event.as_dict() for event in events]
  as_json= json.dumps(result, default=date_handler, indent=2, ensure_ascii=False)
  return HttpResponse (as_json, content_type="application/json")

@csrf_exempt
@login_required
def get_donation(request, projectid):
  if request.method == "GET":
    return render(request,'donation.html', {
       "projectid": projectid,
    })
  # untuk save data donasi
  if request.method == "POST":
    namadonatur = request.user.username#User.objects.get(username=request.user.username)
    nilaidonasi = request.POST['nilaidonasi']
    tanggaldonasi = datetime.today()
    statusdonasi = 'Belum Terverifikasi'
    try:
      #dari parameter projectid yang direquest user
      current_project=ProjectModel.objects.get(id=projectid)
      #model dengan reference key ke User dan ke Project.
      donasi = DonateModel.objects.create(donatur=request.user,project=current_project)
      donasi.nama_donatur = namadonatur
      donasi.nilai_donasi = nilaidonasi
      donasi.status_donasi = statusdonasi
      donasi.tanggal_donasi = tanggaldonasi
      donasi.save()
    except:
      if donasi != None:
        donasi.delete()
      return HttpResponseRedirect('/donation/?error=registerfail')
    else:
      return HttpResponseRedirect('/confirm_donation/')

@login_required
def confirm_donation(request):
    if request.method == "GET":
      current_user = User.objects.get(id = request.user.id)
      donates = current_user.donations.all()
      result = [donate.as_dict() for donate in donates]
      as_json= json.dumps(result, default=date_handler, indent=2, ensure_ascii=False)
      return HttpResponse (as_json, content_type="application/json")


@csrf_exempt
def register_view(request):
  if request.method == "GET":
    return render(request, 'register.html')

  if request.method == "POST":
    # return
    save_username = request.POST['username']
    save_email = request.POST['email']
    save_firstname = request.POST['firstname']
    save_lastname = request.POST['lastname']
    save_password = request.POST['password']

    try:
      user = User.objects.create_user(save_username,save_email,save_password)
      user.first_name = save_firstname
      user.last_name = save_lastname
      user.save()
    except:
      logger.error('Something went wrong!')
      return HttpResponseRedirect('/register/?error=registerfail')

    else:
      temp_status = "Register Success"
      return HttpResponse(temp_status)
      print(user)


def login_view (request):
  if request.method == "GET":
   # if request.GET['error'] == 'authfail':
    return render(request,'login.html')
  if request.method == "POST":
    username = request.POST['uname']
    password = request.POST['psw']
    user = authenticate(username=username, password=password)

    if user is not None:
    # A backend authenticated the credentials, auth trus login usernya. object user dimasukin request
      login(request, user)
      return HttpResponseRedirect('/profile/')
    else:
    # No backend authenticated the credentials
      return HttpResponseRedirect('/login/?error=authfail')

#@login_required
def profile_view (request):
  #is_authenticated jadi opsi, tapi enak pake login_required.
  if request.user.is_authenticated:
    my_account = request.user
    return render(request, 'profil.html', context={
      'test' : my_account,
    })
  else:
    return HttpResponseRedirect('/login/')

@login_required
def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/login/')

def get_responseCodeList(request):
  responses = ResponseModel.objects.all()
  result = [response.as_dict() for response in responses]
  as_json= json.dumps(result, default=date_handler, indent=2, ensure_ascii=False)
  return HttpResponse (as_json, content_type="application/json")
