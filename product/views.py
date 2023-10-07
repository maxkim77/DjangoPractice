from django.shortcuts import render

def product_contents(request, pk):  # pk 인자 추가
    # 여기에서 pk를 사용하여 필요한 데이터를 가져올 수 있습니다.
    return render(request, 'product_contents.html')

def product_main(request):
    return render(request, 'product_main.html')
