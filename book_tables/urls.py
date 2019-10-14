"""book_tables URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 书籍
    re_path('books/add',views.add_book ),
    re_path('books/$',views.books ),
    re_path('books/(\d+)/change/$',views.chenge_book ),
    re_path('books/(\d+)/delete/$',views.delete_book ),

    # 作者详情
    re_path('authordetails/add',views.add_authordetail ),
    re_path('authordetails/$', views.authordetails),
    re_path('authordetails/(\d+)/delete/$', views.delete_authordetail),
    re_path('authordetails/(\d+)/change/$', views.change_authordetail),

    # 作者
    re_path('authors/add',views.add_author ),
    re_path('authors/$',views.authors ),
    re_path('authors/(\d+)/delete/$', views.delete_author),
    re_path('authors/(\d+)/change/$', views.change_author),

    # 出版社
    re_path('publishs/add', views.add_publish),
    re_path('publishs/$', views.publishs),
    re_path('publishs/(\d+)/delete/$', views.delete_publish),
    re_path('publishs/(\d+)/change/$', views.change_publish),
]
