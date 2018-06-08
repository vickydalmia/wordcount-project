from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hru': 'iAM gOOD'})

def count(request):
    inputText = request.GET['words']
    inputTextList = inputText.split()
    inputTextListLength = len(inputTextList)
    sameWordCount = {}
    for word in inputTextList:
        if word in sameWordCount:
            sameWordCount[word] += 1
        else:
            sameWordCount[word] = 1 

    return render(request, 'count.html', {'inputTextListLength': inputTextListLength, 'inputText': inputText, 'sameWordCount': sameWordCount.items()})

def about(request):
    return render(request, 'about.html')