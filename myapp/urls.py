from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
# ----------------------------__Admin__--------------------------------
    path('index-admin/',views.index_admin,name='index-admin'), 
    path('profile-admin/',views.profile_admin,name='profile-admin'), 
    path('view-seller/',views.view_seller,name='view-seller'),
    path('delete-seller/<int:pk>',views.delete_seller,name='delete-seller'),
    path('verify-seller/<int:pk>',views.verify_seller,name='verify-seller'),
    path('view-buyer/',views.view_buyer,name='view-buyer'),
    path('delete-buyer/<int:pk>',views.delete_buyer,name='delete-buyer'),
    path('verify-buyer/<int:pk>',views.verify_buyer,name='verify-buyer'),

# ----------------------------__Seller__--------------------------------
    path('index-seller/',views.index_seller,name='index-seller'),
    path('add-product',views.add_product,name='add-product'),
    path('view-product',views.view_product,name='view-product'),
    path('edit-product/<int:pk>',views.edit_product,name='edit-product'),
    path('delete-product/<int:pk>',views.delete_product,name='delete-product'),
    path('profile-seller',views.profile_seller,name='profile-seller'),

# ----------------------------__Buyer__--------------------------------
    path('product-filter/<str:id>',views.product_filter,name='product-filter'),
    path('view-product/<int:pk>',views.view_product,name='view-product'),
    path('add-to-cart/<int:pk>',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.cart,name='cart'),
    path('update-cart/<int:pk>',views.update_cart,name='update-cart'),
    path('remove-cart/<int:pk>',views.remove_cart,name='remove-cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('my-order/',views.my_order,name='my-order'),
    path('cancel-order/<int:pk>',views.cancel_order,name='cancel-order'),
    path('profile-buyer',views.profile_buyer,name='profile-buyer'),
    path('change-password',views.change_password,name='change-password'),
    

]
