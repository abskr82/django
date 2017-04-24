from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse('Hello dear')
    return render(request, 'home.html')

def translate(request):
    data = request.GET['inpval']
    translation = ''
    for w in data.split():
        if w[0] in ['a', 'e', 'i', 'o','u']:
            #vowel
            translation += w
            translation += 'yay '            
            
        else:
            # consonant
            translation += w[1:]
            translation += w[0]
            translation += 'ay '
    # return HttpResponse(translation)
    return render(request, 'translate.html', {'original':data, 'translation':translation})
