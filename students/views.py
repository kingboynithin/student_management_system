from django.shortcuts import render


def home(request):
    course_names = [
        "DBMS",
        "OS",
        "WEB TECHNOLOGY",
        "COMPUTER NETWORK",
        "SOFTWARE ENGINEERING",
    ]

    return render(
        request,
        "students/home.html",
        {"course_names": course_names}
    )


def about(request):
    return render(request, "students/about.html")


def contact(request):
    return render(request, "students/contact.html")