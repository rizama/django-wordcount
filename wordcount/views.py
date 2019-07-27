from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordictionary = {}
    for word in wordlist:
        if word in wordictionary:
            # increase
            wordictionary[word] += 1
        else:
            wordictionary[word] = 1
    sorteWord = sorted(wordictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',
                  {
                      'fulltext': fulltext,
                      'count': len(wordlist),
                      'sorteWord': sorteWord,
                  })


def about(request):
    return render(request, 'about.html')