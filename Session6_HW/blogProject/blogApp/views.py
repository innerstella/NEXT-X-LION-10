from django.shortcuts import redirect, render
from .models import Article
from .models import Category
# Create your views here.


def new(request):
    if request.method == "POST":
        # POST 요청으로 온 데이터 확인
        print(request.POST)
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('list')

    return render(request, 'new.html')


def list(request):
    articles = Article.objects.all()
    count = len(articles)
    hobby_count = Article.objects.filter(category='1').count()
    food_count = Article.objects.filter(category='2').count()
    programming_count = Article.objects.filter(category='3').count()

    return render(request, 'list.html', {'articles': articles, 'count': count, 'hobby_count': hobby_count, 'food_count': food_count, 'programming_count': programming_count})


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})


def hobby(request):
    articles = Article.objects.all()
    count = len(articles)
    return render(request, 'hobby.html',
                  {'articles': articles, 'count': count})


def food(request):
    articles = Article.objects.all()
    count = len(articles)
    return render(request, 'food.html', {'articles': articles, 'count': count})


def programming(request):
    articles = Article.objects.all()
    count = len(articles)

    return render(request, 'programming.html', {'articles': articles, 'count': count})
