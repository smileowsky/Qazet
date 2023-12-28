from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . models import News, Comments
from django.contrib import messages
from django.db import connection
from bs4 import BeautifulSoup
import requests
import datetime
from django.db.models import Count

# Create your views here.
cursor = connection.cursor()

date_now = datetime.datetime.now()
formatted_date = date_now.strftime("%d-%m-%Y-%H:%M")
comments_num = Comments.objects.all().count()


def home(request):
    data1 = News.objects.all().order_by('-id')[:4]
    data2 = News.objects.all().order_by('-id')[4:7]
    data3 = News.objects.all().order_by('-id')[7:12]
    data4 = News.objects.all().order_by('-id')[12:15]
    data5 = News.objects.all().order_by('-id')[15:25]
    data6 = News.objects.all().order_by('-id')[25:29]

    news_with_comments = News.objects.annotate(comment_count=Count('comments'))
    sorted_news = news_with_comments.order_by('-comment_count')[:4]

    categories = News.objects.filter(news_category__in=['Siyasət', 'İdman', 'İqtisadiyyat', 'Ölkə', 'Kriminal', 'Qafqaz', 'Sosial', 'Sağlamlıq', 'Texnologiya', 'Şou-biznes']).values('news_category').distinct()
    differents = News.objects.exclude(news_category__in=['Siyasət', 'İdman', 'İqtisadiyyat', 'Ölkə', 'Kriminal', 'Qafqaz', 'Sosial', 'Sağlamlıq', 'Texnologiya', 'Şou-biznes']).values('news_category').distinct()

    return render(request, 'home.html', {'sorted_news' : sorted_news, 'categories': categories, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5, 'data6': data6, 'formatted_date': formatted_date, 'comments_num': comments_num, 'differents': differents})


def category_detail(request, cat_id):
    data = News.objects.filter(news_category=cat_id)
    cat = News.objects.filter(
        news_category=cat_id).order_by('-news_category')[:1]
    data1 = News.objects.filter(news_category=cat_id).order_by('-id')[:6]
    data2 = News.objects.filter(news_category=cat_id).order_by('-id')[6:10]
    data3 = News.objects.filter(news_category=cat_id).order_by('-id')[10:13]
    
    categories = News.objects.filter(news_category__in=['Siyasət', 'İdman', 'İqtisadiyyat', 'Ölkə', 'Kriminal', 'Qafqaz', 'Sosial', 'Sağlamlıq', 'Texnologiya', 'Şou-biznes']).values('news_category').distinct()
    differents = News.objects.exclude(news_category__in=['Siyasət', 'İdman', 'İqtisadiyyat', 'Ölkə', 'Kriminal', 'Qafqaz', 'Sosial', 'Sağlamlıq', 'Texnologiya', 'Şou-biznes']).values('news_category').distinct()

    return render(request, 'categories.html', {'categories': categories, 'differents': differents, 'data': data, 'data1': data1, 'data2': data2, 'data3': data3, 'cat': cat})


def single(request, news_id):
    single = News.objects.get(id=news_id)
    data2 = News.objects.all().order_by('-id')[:6]
    data3 = News.objects.all().order_by('-id')[6:9]
    data = Comments.objects.filter(news_id_id=news_id).order_by('-id')
    number = data.count()
    keywords = single.news_name.split()

    categories = cursor.execute(
        "SELECT news_category FROM main_news WHERE news_category IN ('Siyasət', 'İdman', 'İqtisadiyyat', 'Ölkə', 'Kriminal', 'Qafqaz', 'Sosial', 'Sağlamlıq', 'Texnologiya', 'Şou-biznes') GROUP BY news_category")
    categories = cursor.fetchall()
    differents = cursor.execute(
        "SELECT news_category FROM main_news WHERE news_category NOT IN ('Siyasət', 'İdman', 'İqtisadiyyat', 'Ölkə', 'Kriminal', 'Qafqaz', 'Sosial', 'Sağlamlıq', 'Texnologiya', 'Şou-biznes') GROUP BY news_category")

    return render(request, 'single.html', {'categories': categories, 'differents': differents, 'keywords': keywords, 'single': single, 'data2': data2, 'data3': data3, 'data': data, 'number': number})


def news(request):
    if 'take_it_qafqaz' in request.POST:
        source = 'qafqazinfo.az'
        data_from = requests.get('https://www.qafqazinfo.az/')
        soup = BeautifulSoup(data_from.text, 'html.parser')
        data_from = soup.find_all('ul', class_='sonxeber')

        if data_from:
            links = data_from[1].find_all('a')

            for x in links:
                link = x['href']

                data = requests.get(link)
                soup = BeautifulSoup(data.text, 'html.parser')

                title_element = soup.find_all('div', class_='panel-body')
                title = title_element[0].find('h2').text

                image_element = soup.find('img', class_='img-responsive')
                image = image_element['src']

                category_element = soup.find(
                    'div', class_='col-lg-3 col-md-3 col-sm-3 col-xs-3')
                category = category_element.find('a').text

                text_element = soup.find('div', class_='news_text')
                text = text_element.find('p').text

                if link and title and image and category and text:

                    if News.objects.filter(news_link=link).count() == 0:
                        news_info = News(
                            news_name=title,
                            news_link=link,
                            news_text=text,
                            news_source=source,
                            news_category=category,
                            news_image=image
                        )
                        news_info.save()

    if 'take_it_milli' in request.POST:
        source = 'milli.az'
        data_from = requests.get('https://www.milli.az/')
        soup = BeautifulSoup(data_from.text, 'html.parser')
        data_from = soup.find_all('ul', class_='post-list2')

        if data_from:
            links = data_from[1].find_all('a')
            for x in links:
                link = x['href']

                data = requests.get(link)
                soup = BeautifulSoup(data.text, 'html.parser')

                title = soup.find('h1').text

                image_element = soup.find('img', class_='content-img')
                try:
                    image = image_element['src']
                except TypeError:
                    print('Failed link: '+link)

                category_element = soup.find('div', class_='quiz-holder')
                try:
                    category = category_element.find('span').text
                except AttributeError:
                    print('Failed link: '+link)

                text_element = soup.find('div', class_='article_text')

                try:
                    text = text_element.find('p').text
                except AttributeError:
                    print('Failed link: '+link)

                if link and title and image and category and text:
                    if not News.objects.filter(news_link=link).exists():
                        news_info = News(
                            news_name=title,
                            news_link=link,
                            news_text=text,
                            news_source=source,
                            news_category=category,
                            news_image=image
                        )
                        news_info.save()
    if 'delete' in request.POST:
        News.objects.all().delete()
        messages.info(request, 'Deleting was successfull',
                      extra_tags='success')

    data = News.objects.all().order_by('-id')
    return render(request, 'news.html', {'data': data})


def comments(request, news_id):

    if 'submit' in request.POST:

        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        text = request.POST['text']

        if name and surname and email and text:
            news = News.objects.get(id=news_id)
            comment_info = Comments(
                user_name=name,
                user_surname=surname,
                user_email=email,
                user_comment=text,
                news_id=news
            )
            comment_info.save()
            print('Success')
        else:
            print('Empty')

    return HttpResponseRedirect('/single/'+str(news_id))