from django.shortcuts import render, redirect
from .models import Detail
from .forms import DetailForm
from django.contrib import messages
# Create your views here.



def DetailView(request):
    
    if request.method == "GET":
        form = DetailForm()
        
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.save()
            messages.success(request,'User Details Saved')
            return redirect('detail')

    return render(request,'userauth/detail.html',{'form':form})


def SearchView(request):
    context = {}
    if request.method == "GET":
        search_keyword = request.GET.get('search',None)
        if search_keyword:
            qs = Detail.objects.filter(name__icontains=search_keyword)
            context = {'data':qs.all(),
                'count':qs.count()
            }
            messages.success(request,f'Total no of search result {qs.count()}')
        else:
            messages.warning(request,'Please enter the keyword for search operation')

    return render(request,'search/search.html',context)


def get_images(request):
    return render(request,'userauth/show_image.html')



