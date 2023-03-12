from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import student
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail
import imaplib,email
p_email=''
flag=0
d={
    'stat':'NO'
}
# Create your views here.
def regiister(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'appauth/register.html',{'form':form})
   

@login_required
def home(request):
    d4=student.objects.filter(booked_by=request.user).last()
    if(d4.closed == True):
        if request.method=='POST':
            bk=request.user
            nm=request.POST.get('N_ame')
            adm=request.POST.get('admisno')
            em=request.POST.get('e_mail')
            pem=request.POST.get('pe_mail')
            phn=request.POST.get('phone')
            pphn=request.POST.get('parphone')
            gndr=request.POST.get('Gender')
            bnch=request.POST.get('Branch')
            yr=request.POST.get('ye_ar')
            l_tpe=request.POST.get('type')
            l_dteF=request.POST.get('datef')
            l_dteT=request.POST.get('datet') 
            l_reas=request.POST.get('resn')
            stud=student.objects.create(booked_by=bk,name=nm,admno=adm,email=em,paremail=pem,phno=phn,p_phno=pphn,sex=gndr,branch=bnch,year=yr,l_type=l_tpe,l_datefrom=l_dteF,l_dateto=l_dteT,l_rsn=l_reas)
            stud.save()
            p_email=pem
            send_mail(
            'Regarding the issue of outpass',
            'This is a Test mail sent with the help of django package.',
            '2020cs0279@svce.ac.in',
            [p_email],
            fail_silently=False,
            )
    else:
        messages.error(request,'Open form already exists,try again')
    return render(request,'appauth/hostelapp.html')

def display(request):
    d1={
        'd2':student.objects.filter(booked_by=request.user)
    }
    return render(request,'appauth/disp.html',d1)

def statue(request,str):
    print(str)
    yy=student.objects.filter(booked_by=request.user).last()
    yy.closed=str
    yy.save()
    return redirect('display')

def profile(request):
   if(flag==0):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('2020cs0279@svce.ac.in', 'ilovemyFAMILY7&')
        mail.select('INBOX')
        result,raw_data=mail.search(None,'(OR (SUBJECT "Regarding the issue of outpass") (FROM p_email))')
        ids = raw_data[0] # data is a list.
        id_list = ids.split() # ids is a space separated string
        latest_email_id = id_list[-1] # get the latest

        result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message=email.message_from_string(raw_email_string)
        for p in email_message.walk():
            if p.get_content_type() == "text/plain":
                body=p.get_payload()
        f=body.split(',')

        yy=student.objects.filter(booked_by=request.user).last()
        print(f[0])
        if(f[0]=="Yes"):
            yy.permit_allowed=True
            yy.save()
        else:
            yy.permit_allowed=False
            yy.save()
   return render(request,'appauth/profile.html',{'x':yy})
#if student.objects.filter(booked_by=request.user).exists():
#        return HttpResponse('Not possible')
#    else: