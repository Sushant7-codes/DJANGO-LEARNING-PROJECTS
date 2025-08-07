from django.shortcuts import render


class Demo:
    def __init__(self):
        self.value="default value"
        
        
# Create your views here.
def home(request):
    
    # var1 = "This is from var1"
    # username= "SUSHANT@1234567890"
    
    user ={"name":"Sushant","age":21}
    interest=["coding","football"]
    demo_obj = Demo()
    
    
    context={
        'user':user,
        'user_interest':interest,
        'demo_obj':demo_obj
    }
    return render(request, 'app/home.html',context)

def posts(request):
    
    user_role=""
    
    posts_data = [
         {
             'title':"Happy birthday",
             'caption':"Enjoying the party",
             'tags':["ram","shyam","hari"]
         },
         {
             'title':"Congratulations",
             'caption':"congratulating you",
             'tags':["ram","hari"]
         },
         {
             'title':"happy new year",
             'caption':"Enjoying the new year party",
             'tags':["ram","shyam","hari"]
         },
    ]
    
    demo =""
    context = {
        'data':posts_data,
        'user_role':user_role,
        'demo':demo
    }
    return render (request, 'app/posts.html', context)