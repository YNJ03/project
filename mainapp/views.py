from django.shortcuts import render
from django.http import HttpResponse
### UME 시각화를 처리하는 라이브러리
from mainapp.cme_view.cme import Cme_View

def Details_sunspot(request) :
    return render(request, "mainapp/data_view/details_sunspot.html", {})

def Index(request) :
    return render(request, "mainapp/index.html", {})

def Details_cme(request) :
    return render(request, "mainapp/data_view/details_cme.html", {})

def Details_cme2(request) :
    
    if request.POST.get("select") is not None :
        select = request.POST.get("select")
        select_list = request.POST.getlist("select")

        str_list = ""
        
        for i in range(len(select_list)) :
            str_list += select_list[i]
            if i < len(select_list)-1 :
                str_list += "_"
            
        url = "/static/mainapp/img/portfolio/UME/UME_{}.png".format(str_list) 
    return render(request, "mainapp/data_view/details_cme2.html", {"select" : select, "select_list" : select_list, "str_list" : str_list, "url" : url})

def Details_kp(request) :
    return render(request, "mainapp/data_view/details_kp.html", {})

def Details_kp2(request) :
    if request.POST.get("select") is not None :
        select = request.POST.get("select")
        select_list = request.POST.getlist("select")

        str_list = ""
        
        for i in range(len(select_list)) :
            str_list += select_list[i]
            if i < len(select_list)-1 :
                str_list += "_"
            
        url = "/static/mainapp/img/portfolio/kp/{}.png".format(str_list) 
    return render(request, "mainapp/data_view/details_kp2.html", {"select" : select, "select_list" : select_list, "str_list" : str_list, "url" : url})

def Details_frequency(request) :
    return render(request, "mainapp/data_view/details_frequency.html", {})

def Details_frequency2(request) :
    if request.POST.get("select") is not None :
        select = request.POST.get("select")
        select_list = request.POST.getlist("select")

        str_list = ""
        
        for i in range(len(select_list)) :
            str_list += select_list[i]
            if i < len(select_list)-1 :
                str_list += "_"
            
        url = "/static/mainapp/img/portfolio/frequency/{}.png".format(str_list) 
    
    return render(request, "mainapp/data_view/details_frequency2.html", {"select" : select, "select_list" : select_list, "str_list" : str_list, "url" : url})

def Details_xline(request) :
    return render(request, "mainapp/data_view/details_xline.html", {})

def Details_xline2(request) :
    if request.POST.get("select") is not None :
        select = request.POST.get("select")
        select_list = request.POST.getlist("select")

        str_list = ""
        
        for i in range(len(select_list)) :
            str_list += select_list[i]
            if i < len(select_list)-1 :
                str_list += "_"
            
        url = "/static/mainapp/img/portfolio/xline/{}.png".format(str_list) 
    return render(request, "mainapp/data_view/details_xline2.html", {"select" : select, "select_list" : select_list, "str_list" : str_list, "url" : url})

def Details_thermo(request) :
    return render(request, "mainapp/data_view/details_thermo.html", {})

def Details_thermo2(request) :
    
    if request.POST.get("select") is not None :
        select = request.POST.get("select")
        select_list = request.POST.getlist("select")

        str_list = ""
        
        for i in range(len(select_list)) :
            str_list += select_list[i]
            if i < len(select_list)-1 :
                str_list += "_"
            
        url = "/static/mainapp/img/portfolio/thermosphere/{}.png".format(str_list) 
    return render(request, "mainapp/data_view/details_thermo2.html", {"select" : select, "select_list" : select_list, "str_list" : str_list, "url" : url})

def Details_elino(request) :
    return render(request, "mainapp/data_view/details_elino.html", {})

def Details_elino2(request) :
    if request.POST.get("select") is not None :
        select = request.POST.get("select")
        select_list = request.POST.getlist("select")

        str_list = ""
        
        for i in range(len(select_list)) :
            str_list += select_list[i]
            if i < len(select_list)-1 :
                str_list += "_"
            
        url = "/static/mainapp/img/portfolio/elino/{}.png".format(str_list) 
    return render(request, "mainapp/data_view/details_elino2.html", {"select" : select, "select_list" : select_list, "str_list" : str_list, "url" : url})

def Details_radioflux(request) :
    return render(request, "mainapp/data_view/details_radioflux.html", {})

def Details_radioflux2(request) :
    if request.POST.get("select") is not None :
        select = request.POST.get("select")
        select_list = request.POST.getlist("select")

        str_list = ""
        
        for i in range(len(select_list)) :
            str_list += select_list[i]
            if i < len(select_list)-1 :
                str_list += "_"
            
        url = "/static/mainapp/img/portfolio/radioflux/{}.png".format(str_list) 
    return render(request, "mainapp/data_view/details_radioflux2.html", {"select" : select, "select_list" : select_list, "str_list" : str_list, "url" : url})

def any2(request) :
    return render(request, "mainapp/any2.html", {})

def silsi(request) :
    return render(request, "mainapp/silsi_view.html", {})

def silsi2(request) :
    return render(request, "mainapp/silsi_view2.html", {})

def Details(request) :
    return render(request, "mainapp/portfolio-details.html", {})

def Details2(request) :
    return render(request, "mainapp/portfolio-details2.html", {})

def Details3(request) :
    return render(request, "mainapp/portfolio-details3.html", {})

def Details4(request) :
    return render(request, "mainapp/portfolio-details4.html", {})

def Details5(request) :
    return render(request, "mainapp/portfolio-details5.html", {})

def sun3_4(request) :
    return render(request, "mainapp/data_view/sun3_4.html", {})
   
def sun3_3(request) :
    return render(request, "mainapp/data_view/sun3_3.html", {})
   
def sun3_2(request) :
    return render(request, "mainapp/data_view/sun3_2.html", {})
   
def sun3_1(request) :
    return render(request, "mainapp/data_view/sun3_1.html", {})
   
def sun2_1(request) :
    return render(request, "mainapp/data_view/sun2_1.html", {})
   
def sun1_2(request) :
    return render(request, "mainapp/data_view/sun1_2.html", {})
   
def sun1_1(request) :
    return render(request, "mainapp/data_view/sun1_1.html", {})