from django.shortcuts import render
from formapp.Forms import NewUserforms

def index(requests):
    voot ={"lol":'Im from index.html'}
    return render(requests,'index.html',context=voot)


def help(requests):

    form = NewUserforms()

    if requests.method == "POST":
         form = NewUserforms(requests.POST)

         if form.is_valid():
            form.save(commit=True)
            return index(requests)
         else:
            print("ERROR FORM INVALID")

    return render(requests, 'Fromname.html',{'form':form})


