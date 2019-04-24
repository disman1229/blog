from django.shortcuts import render

# Create your views here.
def index(request):
    title:'文章列表'
    context:{'title':title}
    print (type(context))
    return render(request, 'myblog/article_list.html',context)