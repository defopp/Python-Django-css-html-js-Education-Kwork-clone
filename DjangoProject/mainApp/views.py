from django.shortcuts import render

# Create your views here.
def MainPage(request):
    return render(request, 'mainApp\\main.html')

def ToFreelancerPage(request):
    return render(request, 'mainApp\\to_freelancer.html')
