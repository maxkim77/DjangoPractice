from django.shortcuts import render

def qna_contents(request, pk):
    return render(request, 'qna_contents.html')

def qna_main(request):
    return render(request, 'qna_main.html')