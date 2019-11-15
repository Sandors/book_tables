from django.shortcuts import render,HttpResponse,redirect
from books.models import *
from django.core.paginator import Paginator,EmptyPage   # 分页器


# Create your views here.


def add_book(request):
	if request.method == "POST":
		title=request.POST.get("title")
		price=request.POST.get("price")
		pub_date=request.POST.get("pub_date")
		publish_id=request.POST.get("publish_id")
		authors_id_list=request.POST.getlist("authors_id_list") # checkbox select 多选

		book_obj=Books.objects.create(title=title,price=price,publishDate=pub_date,publish_id=publish_id)
		print(authors_id_list)

		book_obj.authors.add(*authors_id_list)  # 绑定多对多关系

		return redirect('/books/')

	publish_list = Publish.objects.all()
	author_list = Author.objects.all()

	return render(request,"add_book.html",{"publish_list":publish_list,"author_list":author_list})

def books(request):
	book_list=Books.objects.all()

	# 分页器
	paginator=Paginator(book_list,2)
	# print('page_range',paginator.page_range)
	# print('num_pages',paginator.num_pages)
	current_page_num = int(request.GET.get("page", 1))
	# 控制页数数量
	if paginator.num_pages > 11:
		if current_page_num -5 < 1:
			page_range=range(1,12)
		elif current_page_num + 5 > paginator.num_pages:
			page_range=range(paginator.num_pages-10,paginator.num_pages+1)
		else:
			page_range=range(current_page_num-5,current_page_num+6)
	else:
		page_range=paginator.page_range

	try:

		current_page=paginator.page(current_page_num)
	except EmptyPage as e:
		current_page_num=paginator.page(1)


	return render(request,"books.html",locals())
	# return render(request,"books.html",{"book_list":book_list,"current_page":current_page,"current_page_num":current_page_num,"paginator":paginator})

def chenge_book(request,edit_book_id):
	edit_book_obj = Books.objects.filter(pk=edit_book_id).first()
	if request.method == "POST":
		title=request.POST.get("title")
		price=request.POST.get("price")
		pub_date=request.POST.get("pub_date")
		publish_id=request.POST.get("publish_id")
		authors_id_list=request.POST.getlist("authors_id_list")

		Books.objects.filter(pk=edit_book_id).update(title=title,price=price,publishDate=pub_date,publish_id=publish_id)

		# edit_book_obj.authors.clear()
		# edit_book_obj.authors.add(*authors_id_list)
		edit_book_obj.authors.set(authors_id_list)

		return  redirect("/books/")

	publish_list = Publish.objects.all()
	author_list = Author.objects.all()
	return render(request,"edit_book.html",{"edit_book_obj":edit_book_obj,"publish_list":publish_list,"author_list":author_list})

def delete_book(request,delete_book_id):

	Books.objects.filter(pk=delete_book_id).delete()

	return redirect("/books/")


def add_authordetail(request):
	if request.method=="POST":
		birthday=request.POST.get("birthday")
		telephone=request.POST.get("telephone")
		addr=request.POST.get("addr")
		authorDetail_obj=AuthorDetail.objects.create(birthday=birthday,telephone=telephone,addr=addr)

		return redirect("/authordetails/")

	return render(request,"add_authordetail.html")

def authordetails(request):
	authordetail_list=AuthorDetail.objects.all()

	return render(request,"authordetails.html",{"authordetail_list":authordetail_list})

def delete_authordetail(request,delete_authordetail_id):

	AuthorDetail.objects.filter(pk=delete_authordetail_id).delete()

	return redirect("/authordetails/")

def change_authordetail(request,edit_authordetail_id):

	authordetail_obj=AuthorDetail.objects.filter(pk=edit_authordetail_id).first()
	if request.method=="POST":
		birthday=request.POST.get("birthday")
		telephone=request.POST.get("telephone")
		addr=request.POST.get("addr")

		AuthorDetail.objects.filter(pk=edit_authordetail_id).update(birthday=birthday,telephone=telephone,addr=addr)
		return redirect('/authordetails/')
	return render(request,"edit_authordetail.html",{"authordetail_obj":authordetail_obj})


def add_author(request):
	if request.method=="POST":
		name=request.POST.get("name")
		age=request.POST.get("age")
		authordetail_id=request.POST.get("authordetail_id")

		author_obj=Author.objects.create(name=name,age=age,authorDetail_id=authordetail_id)

		return redirect("/authors/")

	authordetail_list=AuthorDetail.objects.all()

	return render(request,"add_author.html",{"authordetail_list":authordetail_list})

def authors(request):

	author_list=Author.objects.all()
	return render(request,"author.html",{"author_list":author_list})

def delete_author(request,delete_author_id):
	Author.objects.filter(pk=delete_author_id).delete()
	return redirect('/authors/')

def change_author(request,edit_author_id):

	author_obj=Author.objects.filter(pk=edit_author_id).first()
	if request.method=="POST":

		name=request.POST.get("name")
		age=request.POST.get("age")
		authordetail_id=request.POST.get("authordetail_id")
		Author.objects.filter(pk=edit_author_id).update(name=name,age=age,authorDetail=authordetail_id)
		return redirect('/authors/')


	author_list=Author.objects.all()
	authordetail_list=AuthorDetail.objects.all()

	list_author=[]
	all_author_object=Author.objects.all().values('authorDetail_id')
	all_author_list_dic=list(all_author_object)
	for i in all_author_list_dic:
		list_author.append(i["authorDetail_id"])
	list_author.remove(author_obj.authorDetail_id)

	list_authordetail=[]
	all_authordetial_object = AuthorDetail.objects.all().values('nid')
	all_authordetial_list_dic = list(all_authordetial_object)

	for i in all_authordetial_list_dic:
		list_authordetail.append(i["nid"])

	list1=[i for i in list_authordetail if i not in list_author]

	return render(request,"edit_author.html",{"author_obj":author_obj,"author_list":author_list,"authordetail_list":authordetail_list,"list1":list1})


def add_publish(request):
	if request.method=="POST":
		name=request.POST.get("name")
		city=request.POST.get("city")
		email=request.POST.get("email")
		publish_obj=Publish.objects.create(name=name,city=city,email=email)
		return redirect("/publishs/")
	return render(request,"add_publish.html")

def publishs(request):
	publish_list=Publish.objects.all()
	return render(request,"publishs.html",{"publish_list":publish_list})

def delete_publish(request,delete_publish_id):
	Publish.objects.filter(pk=delete_publish_id).delete()
	return redirect('/publishs/')

def change_publish(request,change_publish_id):
	publish_object=Publish.objects.filter(pk=change_publish_id).first()
	if request.method=="POST":
		name=request.POST.get("name")
		city=request.POST.get("city")
		email=request.POST.get("email")
		Publish.objects.filter(pk=change_publish_id).update(name=name,city=city,email=email)

		return redirect('/publishs/')

	return render(request,"edit_publish.html",{"publish_object":publish_object})