from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext1 = request.GET['fulltext']
    wordlist = fulltext1.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]= 1
    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'fulltext1':fulltext1,'count':len(wordlist),'dict':sortedwords})
