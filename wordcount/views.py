from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', )


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    # set up an empty dictionary
    worddictionary = {}

    # loop through the wordlist, checking if each word is already in the dictionary, tallying up as you go
    for word in wordlist:
        if word in worddictionary:
            # increment
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1

    # convert the dictionary to a list by appending '.list()' to it, to sort, wrap in a sorted() fn

    sortedwords = sorted(worddictionary.items(),
                         key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, "count": len(wordlist), "sortedwords": sortedwords})


def about(request):
    return render(request, 'about.html', )
