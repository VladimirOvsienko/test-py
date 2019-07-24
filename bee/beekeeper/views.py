from django.shortcuts import render


# from django.http import HttpResponse


def beet(request):
    header = 'personal data'
    langs = ['English', 'German', 'Spanish']
    user = {'name': 'Tom', 'age': 23}
    addr = ('abricosovay', 23, 45)

    data = {'header': header, 'langes': langs, 'user': user, 'address': addr}
    return render(request, "bee/home.html", context=data)

    # def index (request):
# return HttpResponse('<h2>hello world</h2>')
