from django.shortcuts import render

# Create your views here.
def post_list(request):
    
    print "hi Zheng Xu"
    return render(request, 'blog/post_list.html', {})