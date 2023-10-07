from django.shortcuts import render

def free_contents(request, pk):
    return render(request, 'free_contents.html')
def free_main(request):
    return render(request, 'free_main.html')
def notice(request):
    return render(request, 'notice.html')
def oneone_main(request):
    return render(request, 'oneone_main.html')
def oneone_contents(request, pk):
    return render(request, 'oneone_contents.html')