from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from myapp.forms import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{"product":product})


def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Are Register Sucessfully Wait Until Your ID Is Verified')
            return redirect('index')
        else:
            messages.error(request,form.errors)
            return render(request,'register.html',{'form':form})
    else:
        form =RegisterForm()
    return render(request,'register.html',{'form':form})

def user_login(request):
    # if request.user.is_authenticated:
    #     if request.user.role == 'admin':
    #         return redirect('index_admin')
    #     else:
    #         return redirect('index')
    # else:
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email = form.cleaned_data['email'],password = form.cleaned_data['password'])
            if user is not None:
                if user.verify ==True:
                    if user.is_staff == True:
                        login(request, user)
                        return redirect('index-admin')
                    elif user.role =='seller':
                        login(request, user)
                        return redirect('index-seller')
                    else:
                        login(request, user)
                        return redirect('index')
                else:
                    messages.info(request,'Your account not verify Yet,Please Wait sometime')
                    logout(request)
                    return redirect('login')
            else:
                messages.info(request,'Invalid Email and Password')
                return render(request,'login.html',{'form':form})
        messages.info(request,'Invalid Email and Password')
        return render(request,'login.html',{'form':form})
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')


# ----------------------------__Admin__--------------------------------
@login_required(login_url='/login/')
def index_admin(request):
    return render(request,'superadmin/index.html')


@login_required(login_url='/login/')
def profile_admin(request):
    profile = User.objects.get(id=request.user.id)
    form = ProfileForm(instance=profile)
    return render(request,'superadmin/profile.html',{'form':form})


@login_required(login_url='/login/')
def view_seller(request):
    uid = User.objects.filter(role = 'seller')
    return render(request,'superadmin/view-seller.html',{'uid':uid})


@login_required(login_url='/login/')
def delete_seller(request,pk):
    seller = User.objects.get(id=pk)
    seller.delete()
    messages.info(request,'Seller Sucessfully Delete')
    return redirect('view-seller')

@login_required(login_url='/login/')
def verify_seller(request,pk):
    uid = User.objects.get(id=pk)
    if uid.verify == True:
        messages.info(request,'Seller Already Verify')
        return redirect('view-seller')
    else:
        uid.verify = True 
        uid.save()
        messages.info(request,"Seller Verify ")
        return redirect('view-seller')


@login_required(login_url='/login/')
def view_buyer(request):
    uid = User.objects.filter(role = 'buyer')
    return render(request,'superadmin/view-buyer.html',{'uid':uid})



@login_required(login_url='/login/')
def delete_buyer(request,pk):
    buyer = User.objects.get(id=pk)
    buyer.delete()
    messages.info(request,'Seller Sucessfully Delete')
    return redirect('view-buyer')


@login_required(login_url='/login/')
def verify_buyer(request,pk):
    uid = User.objects.get(id=pk)
    if uid.verify == True:
        messages.info(request,'Buyer Already Verify')
        return redirect('view-buyer')
    else:
        uid.verify = True 
        uid.save()
        messages.info(request,"Buyer Verify ")
        return redirect('view-buyer')




# ----------------------------__Seller__--------------------------------
@login_required(login_url='/login/')
def index_seller(request):
    return render(request,'seller/seller-index.html')


@login_required(login_url='/login/')
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.seller = request.user
            temp.save()
            messages.success(request,'Product Added Sucessfully')
            return redirect('add-product')
        else:
            print(form.errors)
            messages.error(request,form.errors)
            return render(request,'seller/add-product.html',{'form':form})

    else:
        form = ProductForm()
    return render(request,'seller/add-product.html',{'form':form})




@login_required(login_url='/login/')
def view_product(request):
    uid = Product.objects.filter(seller__id = request.user.id)
    return render(request,'seller/view-product.html',{'uid':uid})



@login_required(login_url='/login/')
def edit_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method =="POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,"Your product is Update")
            return redirect('view-product')
        else :
            messages.info(request,"invalid data")
            return render(request,'seller/edit-product.html',{'form':form})     
    else:
        form = ProductForm(instance=product)
    return render(request,'seller/edit-product.html',{'form':form})


@login_required(login_url='/login/')
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    messages.info(request,'Your product is Delete ')
    return redirect('view-product')



@login_required(login_url='/login/')
def profile_seller(request):
    profile = User.objects.get(id=request.user.id)
    if request.method =="POST":
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Your profile is Update")
            return redirect('profile-seller')
        else :
            print(form.errors)
            messages.info(request,"invalid data")
            return render(request,'seller/profile.html',{'form':form})
    else:
        form = ProfileForm(instance=profile)
    return render(request,'seller/profile.html',{'form':form})



# -------------------------Buyer--------------------------------
def product_filter(request,id):
    
    product = Product.objects.all() 
    if id =='1':
        product = Product.objects.filter(category='fashion')
        return render(request,'index.html',{'product':product})
    
    elif id =='2':
       product = Product.objects.filter(category='electronic')
       return render(request,'index.html',{'product':product})
   
    elif id =='3':
        product = Product.objects.filter(category='home and kitchen')
        return render(request,'index.html',{'product':product})
    elif id =='4':
        product = Product.objects.filter(category='travel')
        return render(request,'index.html',{'product':product})

    elif id =='5':
        product = Product.objects.filter(category='toy')
        return render(request,'index.html',{'product':product})
    
    elif id =='6':
        product = Product.objects.filter(category='beauty') 
        return render(request,'index.html',{'product':product})   
    
    elif id =='7':
        product = Product.objects.filter(category='food')
        return render(request,'index.html',{'product':product})
    
    else: 
        product = Product.objects.filter(category='stationery')
        return render(request,'index.html',{'product':product}) 


@login_required(login_url='/login/')
def view_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.user.is_authenticated:
        cart = Mycart.objects.filter(product_id= product, user=request.user).exists()
        return render(request,'buyer/details.html',{'product':product,'cart':cart})
    return render(request,'buyer/details.html',{'product':product})
    


@login_required(login_url='/login/')
def add_to_cart(request,pk):
    product = Product.objects.get(id=pk)
    if request.method =='POST':
        form = MycartForm(request.POST)
        quantity = int(request.POST['quantity'])
        if product.quantity >= quantity:
            if form.is_valid():
                form1 = form.save(commit=False)
                form1.user = request.user
                form1.product = product
                form1.save()
                messages.success(request,"Product Add to Cart")
                return redirect('cart')
        else:
            messages.info(request,"Your Quantity is more than available Quantity ")
            return render(request,'buyer/details.html',{'product':product})  
    return render(request,'buyer/details.html',{'product':product})


@login_required(login_url='/login/')
def cart(request):
    cart = Mycart.objects.filter(user = request.user)
    count = Mycart.objects.filter(user = request.user).count()
    amount=0.0
    for c in cart:
        total=(c.quantity*c.product.price)
        amount +=total   
    final = 150 +amount
    return render(request,'buyer/cart.html',{'cart':cart,'count':count,'amount':amount,'final':final})

@login_required(login_url='/login/')
def update_cart(request,pk):
    cart = Mycart.objects.get(id=pk)
    quantity = request.POST['quantity']
    cart.quantity = quantity 
    cart.save()
    messages.info(request,"Product is Update successfully")
    return redirect('cart')

@login_required(login_url='/login/')
def remove_cart(request,pk):
    cart = Mycart.objects.get(id=pk)
    cart.delete()
    messages.info(request,"Product is deleted ")
    return redirect('cart')

@login_required(login_url='/login/')
def checkout(request):
    cart = Mycart.objects.filter(user = request.user)
    amount=0.0
    for c in cart:
        total=(c.quantity*c.product.price)
        amount +=total   
    final = 150 +amount
    if request.method =="POST":
        for data in cart:
            form = CheckoutForm(request.POST)
            if form .is_valid():
                form1 = form.save(commit=False)
                form1.buyer = request.user
                form1.product = data.product
                form1.total_amount = final 
                form1.quantity = data.quantity
                form1.save()
                data.product.quantity -= data.quantity
                data.product.save()
                data.delete()
            else:
                messages.info(request,"Invalid Data")
                return render(request,'buyer/checkout.html',{'cart':cart,'final':final,'form':form})
                
        messages.info(request,"You have Sucessfully Purchase This Product")
        return redirect('my-order')
    else:
        form = CheckoutForm()
    return render(request,'buyer/checkout.html',{'cart':cart,'final':final,'form':form})


@login_required(login_url='/login/')
def my_order(request):
    buy = Buyproduct.objects.filter(buyer = request.user)
    count = Buyproduct.objects.filter(buyer = request.user).count
    return render(request,'buyer/my-oder.html',{'buy':buy,'count':count})

@login_required(login_url='/login/')
def cancel_order(request,pk):
    order = Buyproduct.objects.get(id=pk)
    order.delete()
    messages.info(request,'Your order is Cancel ')
    return redirect('my-order')


def profile_buyer(request):
    profile = User.objects.get(id=request.user.id)
    if request.method == "POST":
        pass
    else:
        form = ProfileForm(instance=profile)
    return render(request,'buyer/profile.html',{"form":form})


@login_required(login_url='/login/')
def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            form.save()
            messages.success(request,'your password update')
            return redirect('login')
        else:
            messages.error(request,form.errors)
            return render(request,'buyer/change-password.html',{'form':form})   
    else:
        form =PasswordChangeForm(user=request.user)
    return render(request,'buyer/change-password.html',{'form':form}) 
