from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.views import View

# print(make_password('1234'))
# print(check_password('12345',
# 'pbkdf2_sha256$390000$VCL00yn512G6DLNxmDe3BD$6S2NUgSurExNZCy5lfSNpAO+bpuz+LpDuF+DhG7LyK8='))

# Create your views here.
def index(request):

    products = None
    categories = Category.get_all_categories();
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID);
    else:
        products = Product.get_all_products();

    data = {}
    data['products']=products
    data['categories']=categories
    return render(request, 'index.html', data)
    #return render(request, 'orders/order.html')
    #return render(request, 'index.html', {'products':products})


def validateCustomer(customer):
    error_message = None;
    if (not customer.first_name):
        error_message = "First Name Required!!"
    elif len(customer.first_name) < 3:
        error_message = 'First name must be 3 characters long or more'
    elif (not customer.last_name):
        error_message = "Last Name Required!!"
    elif len(customer.first_name) < 3:
        error_message = 'Last name must be 3 characters long or more'
    elif (not customer.phone):
        error_message = "Phone Number Required!!"
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must be 10 characters'
    elif (not customer.email):
        error_message = "Email ID Required!!"
    elif len(customer.email) < 5:
        error_message = 'Enter a valid Email ID!!'
    elif customer.isExists():
        error_message = 'Email ID already registered!'
    elif (not customer.password):
        error_message = "Password Required!!"
    elif len(customer.password) < 8:
        error_message = 'Password must be 8 characters long or more'

    return error_message


class signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = validateCustomer(customer)

        if not error_message:

            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'Signup.html', data)


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid!!'
        else:
            error_message = 'Email or Password invalid!!'
        return render(request, 'login.html', {'error': error_message})





