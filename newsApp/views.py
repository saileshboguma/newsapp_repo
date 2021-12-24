from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def moviesinfo(request):
    head_msg='Latest Movies Information'
    msg1='RRR'
    msg2='Pushpa'
    msg3='Radhe Shyam'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest Sports Information'
    msg1='Kohil retier form T20'
    msg2='India Win the Match'
    msg3='India team coach has been change'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request,'newsApp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg='Latest politics Information'
    msg1='YSRCP'
    msg2='TDP'
    msg3='BJP'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request,'newsApp/news.html',context=my_dict)
