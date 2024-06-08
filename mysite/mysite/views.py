from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse('''<h1>hello tanishk</h1> <a href="https://www.youtube.com/watch?v=5gMUWWwYVsM"> Django Song</a>''')

#def about(request):
#    return HttpResponse("hello tanishk")

def index(request):
    #params = {'name':'Love','place':'Mars'}
    
    #return render(request,'index.html',params)
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')
    print(removepunc)
    print(djtext)
    #return HttpResponse("remove punc")
    if removepunc == "on":
        punctations = '''.,?!:;'"&*~'''
        analyzed = ""
        for char in djtext:
            if char not in punctations:
                analyzed = analyzed+char
        params={'purpose':'removepunc','analyze_text':analyzed}
        djtext=analyzed
       # return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Change to Uppercase','analyze_text':analyzed}
        djtext=analyzed
      #  return render(request,'analyze.html',params)
    if(newlineremover=="on"):
        analyzed= ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char.upper()
        params={'purpose':'remove space','analyze_text':analyzed}
        djtext=analyzed
      #  return render(request,'analyze.html',params)
    if(extraspaceremover=="on"):
        analyzed= ""
        for index , char in enumerate(djtext):
            if not (djtext[index]=="" and djtext[index+1]==""):
                analyzed = analyzed + char
            params={'purpose':'remove extra space','analyze_text':analyzed}
    
    if(removepunc != "on" and fullcaps !="on" and newlineremover !="on" and extraspaceremover !="on"):
        return HttpResponse("error")
    
    
    
    
    return render(request,'analyze.html',params)
    
    
            
        
    
    
def ex1(request):
   # s='''<h2>Navigation Bar <br></h2>
   # <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
   # <a href="https://www.facebook.com/"> Facebook </a> <br>
   # <a href="https://www.flipkart.com/"> Flipkart </a> <br>
   # <a href="https://www.hindustantimes.com/"> News </a> <br>
   # <a href="https://www.google.com/"> Google </a> <br>   '''
   # 
   # return HttpResponse(s)
   
   return HttpResponse('''<center><h1>Web-site Directory</h1><table border="1">
            <tr><td>Web-Site Name</td><td>Information</td></tr>
            <tr><td><a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">CODE with Harry</a></td><td>learb django</td></tr>
            <tr><td><a href="https://www.facebook.com/"> Facebook </a></td><td>social Media</td></tr>''')
        
#def capfirst(request):
#    return HttpResponse("captialize first")

#def newlineremove(request):
#    return HttpResponse("remove new line ")

#def spaceremove(request):
#    return HttpResponse("space remover")

#def charcount(request):
#    return HttpResponse("charcount")
#