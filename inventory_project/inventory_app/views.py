import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


# ==========================
# DASHBOARD / HOME
# ==========================
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


# ==========================
# PRODUCTS
# ==========================
@login_required(login_url='login')
def products(request):
    return render(request, 'products.html')


# ==========================
# ORDERS
# ==========================
@login_required(login_url='login')
def orders(request):
    return render(request, 'orders.html')


# ==========================
# ANALYTICS
# ==========================
@login_required(login_url='login')
def analytics(request):
    context = {
        "sales_labels": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        "sales_data": [12, 19, 9, 15, 22, 18, 25],
        "stock_labels": ['Healthy', 'Low', 'Critical'],
        "stock_data": [129, 13, 6],
        "order_labels": ['Pending', 'Shipped', 'Delivered', 'Cancelled'],
        "order_data": [12, 28, 24, 3],
    }
    return render(request, 'analytics.html', context)


# ==========================
# EXPORT CSV
# ==========================
@login_required(login_url='login')
def export_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="inventory_report.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Product Name', 'Category', 'Price', 'Stock', 'Status'])
    writer.writerow(['USB-C Cable', 'Cables', '299', '4', 'Critical'])
    writer.writerow(['Wireless Mouse', 'Accessories', '899', '9', 'Low'])
    writer.writerow(['Laptop Stand', 'Accessories', '1499', '14', 'Low'])
    writer.writerow(['Portable SSD 1TB', 'Storage', '7499', '21', 'Healthy'])
    writer.writerow(['Mechanical Keyboard', 'Electronics', '3499', '32', 'Healthy'])
    writer.writerow(['HDMI Adapter', 'Cables', '499', '6', 'Critical'])

    return response


# ==========================
# LOGIN
# ==========================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')

    return render(request, 'login.html')


# ==========================
# LOGOUT
# ==========================
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('login')


# ==========================
# SIGNUP
# ==========================
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'signup.html')


# ==========================
# ABOUT
# ==========================
def about(request):
    return render(request, 'about.html')


# ==========================
# CONTACT
# ==========================
def contact(request):
    success = False
    error = None
    name_value = ''
    email_value = ''
    message_value = ''

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        name_value = name
        email_value = email
        message_value = message

        subject = f'New Contact Message from {name}'
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            email_msg = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                headers={'Reply-To': email}
            )
            email_msg.send(fail_silently=False)
            success = True
            name_value = ''
            email_value = ''
            message_value = ''
        except Exception as e:
            print(f"Error sending email: {e}")
            error = "Failed to send message. Please try again later."

    return render(request, 'contact.html', {
        'success': success,
        'error': error,
        'name_value': name_value,
        'email_value': email_value,
        'message_value': message_value
    })


# ==========================
# LOADING PAGE
# ==========================
def loading(request):
    return render(request, 'loading.html')