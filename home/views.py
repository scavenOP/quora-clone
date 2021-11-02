from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from home.models import questions,answers

# Create your views here.
def homepage(request):
    all_qs=questions.objects.exclude(author=request.user)
    param={'qs' : all_qs}
    return render(request,'index.html', param)


def handlesignup(request):
    if request.method == 'POST':
        fname=request.POST['namef']
        lname=request.POST['namel']
        username=request.POST['username']
        mail=request.POST['email']
        password=request.POST['pass1']
        myuser=User.objects.create_user(username,mail,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('/')


    else:
        return HttpResponse('404 -Not Found')

def handlelogin(request):
    if request.method == 'POST':
        loginuid=request.POST['uid']
        
        loginpassword=request.POST['loginpass']
        user = authenticate(username=loginuid, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully Logged in")
            return redirect('/')

        else:
            messages.error(request,"Invalid credential")
            return redirect('/')
        
        


    else:
        return HttpResponse('404 -Not Found')

def handlelogout(request):
    
    logout(request)
    return redirect('/')

def handleqssubmit(request):

    q_info=request.POST.get('q_info')
    q_author=request.POST.get('author')
    new_qs=questions(info=q_info,upvote=0,author=q_author)
    new_qs.save()
    return redirect('/')

def handlelike(request):
    if request.user.is_authenticated:
        id=request.POST.get('id')
        
        results = questions.objects.get(q_id=id)
        results.upvote+=1
        results.save()
        return redirect('/')
    else:
        return redirect('/')

def handlequestion(request):

    if request.user.is_authenticated:
        id=request.POST.get('id')
        results = questions.objects.get(q_id=id)
        try:
            all_answer=answers.objects.filter(for_q=id)
        except answers.DoesNotExist:
            all_answer=None
        params={'q':results, 'answers':all_answer}
        return render(request,'question.html',params)

    else:
        
       
        messages.error(request,'You need to login answer a Question')
        return redirect('/')

def handleanswering(request):
    a_info=request.POST.get('ans')
    author=request.POST.get('author')
    q_id=request.POST.get('q_id')
    new_answer=answers(info=a_info,author=author,for_q=q_id)
    new_answer.save()
    messages.success(request,"Answer Added Successfully")
    results = questions.objects.get(q_id=q_id)
    try:
        all_answer=answers.objects.filter(for_q=q_id)
    except answers.DoesNotExist:
        all_answer=None
    params={'q':results, 'answers':all_answer}
    return render(request,'question.html',params)


    

    