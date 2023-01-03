from django.shortcuts import render


# Create your views here.

# FUNCTION BASED VIEW
def setsession(request):
    request.session['name'] = 'Sonam'
    # request.session['lname'] = 'Sharma'
    return render(request, 'setsession.html')


def getsession(request):
    # name = request.session['key']
    name = request.session.get('name')
    # lname = request.session.get('lname')
    # return render(request, 'getsession.html', {'name': name, 'lname': lname})
    return render(request, 'getsession.html', {'name': name})


def delsession(request):
    if 'key' in request.session:
        del request.session['key']
    return render(request, 'delsession.html')

#####################----------- class based view  ------------##################

# class SetSessionView(View):
#     def dispatch(self, request, *args, **kwargs):
#         request.session['name'] = 'Yash'
#         return render(request, 'setsession.html')
#
#
# class GetSessionView(View):
#     def dispatch(self, request, *args, **kwargs):
#         name = request.session.get('name')
#         return render(request, 'getsession.html', {'name': name})
#
#
# class DelSessionView(View):
#     def dispatch(self, request, *args, **kwargs):
#         if 'name' in request.session:
#             del request.session['name']
#         return render(request, 'delsession.html')


# def setsession(request):
#     request.session['name'] = 'Yash'
#     return render(request, 'setsession.html')
#
#
# def getsession(request):
#     name = request.session.get('name')
#     age = request.session.setdefault('age', '26')
#     return render(request, 'getsession.html', {'name': name, 'age': age})
#
#
# def delsession(request):
#     request.session.flush()
#     # if 'key' in request.session:
#     #     del request.session['key']
#     return render(request, 'delsession.html')

def setsession(request):
    request.session['name'] = 'Yash'
    # request.session[0] = 'bar'
    # print(request.session[0])
    # print(request.session['0'])
    # request.session.set_expiry(600)
    # request.session.set_expiry(10)
    return render(request, 'setsession.html')


def getsession(request):
    name = request.session['name']
    return render(request, 'getsession.html', {'name': name})


def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')
