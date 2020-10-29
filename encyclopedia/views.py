from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
import markdown2
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, TITLE):
    if (util.get_entry(TITLE) == None):
        return render(request, "encyclopedia/error.html")
    else:
        ent = markdown2.markdown(util.get_entry(TITLE))
        return render(request, "encyclopedia/entry.html", {
            "entry" : ent,
            "title" : TITLE
        })

def search(request):
    if request.method == "POST":
        search_list = []
        entries = util.list_entries()
        search_word = request.POST["q"]
        if search_word in entries:
            return entry(request, search_word)
        else:
            for word in entries:
                if search_word in word:
                    search_list.append(word)
            if search_list == []:
                return render(request, "encyclopedia/error.html")
            else:
                return render(request, "encyclopedia/search.html", {
                    "entries": search_list
                    })
    else:
        return render(request, "encyclopedia/search.html", {
        "entries": util.list_entries()
    })

def newPage(request):
    if request.method == "POST":
        entries = util.list_entries()
        title = request.POST["title"]
        content = request.POST["content"]
        if title in entries:
            return render(request, "encyclopedia/newPage.html", {
                "message": "The title already exists! please enter another one.",
                "enteredContent": content
            })
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry" ,args=[title]))
    else:
        return render(request, "encyclopedia/newPage.html", {
            "enteredContent": ""
        })

def editPage(request, TITLE):
    if request.method == "POST":
        title = TITLE
        content = request.POST["content"]
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry" ,args=[title]))
    else:
        return render(request, "encyclopedia/editPage.html", {
            "title": TITLE,
            "oldContent": util.get_entry(TITLE)
        })

def randomPage(request):
    entries = util.list_entries()
    randPage = random.randint(0,len(entries)-1)
    page = entries[randPage]
    return HttpResponseRedirect(reverse("entry" ,args=[page]))

        

