from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import bookforms,categoryforms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    error_message = None  # تعريف متغير لتخزين رسالة الخطأ
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # إعادة التوجيه إلى الصفحة الرئيسية
        else:
            error_message = "اسم المستخدم أو كلمة المرور غير صحيحة"

    return render(request, 'login.html', {'error': error_message})   # عرض صفحة تسجيل الدخول

# تأكد من أن المستخدم مسجل للدخول قبل الوصول إلى الصفحة الرئيسية
@login_required
def index(request):
    if request.method == 'POST':
        add_book = bookforms(request.POST, request.FILES)
        add_category = categoryforms(request.POST)

        if add_book.is_valid():
            add_book.save()
        
        if add_category.is_valid():
            add_category.save()

    context = {
       'category': Category.objects.all(),
       'book': Book.objects.all(),
       'form': bookforms(),
       'formcat': categoryforms(),
       'allbooks': Book.objects.filter(active=True).count(),
       'booksold': Book.objects.filter(status='sold').count(),
       'bookbowerd': Book.objects.filter(status='borrowed').count(),
       'bookavilable': Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)
def books(request):
    search=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title :
            search = search.filter(title__icontains=title)
    context = {
        'category':Category.objects.all(),
        'book': search,
       'formcat':categoryforms(),

}
    return render(request, 'pages/books.HTML', context)
def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save=bookforms(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
        return redirect('/')

    else:
        book_save = bookforms(instance=book_id)
    context={
         'form':book_save,
    }     
    return render(request, 'pages/ubdate.HTML', context)    
def delet(request,id):
    book_delet = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_delet.delete()
        return redirect('/')
    return render(request, 'pages/delet.html')
 

    