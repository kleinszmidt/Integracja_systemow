# Blog w Django
### I. Dokumentacja- https://tutorial.djangogirls.org/pl/

### II. Zostało utworzone konto na Python Anywhere- **dzuls**.

### III. Screeny z działania przy projekcie
- Zrzut ekranu z procesem aktywacji wirtualnego środowiska.
![Opis obrazu](srodowisko.png)

- Tą komenda używamy pliku, który został stworzony w naszym folderze aby zainstalować Django. 
`` pip install -r requirements.txt ``
![Opis obrazu](instalowanie.png)


- Poniżej komenda, która utworzyła za mnie katalogii i pliki w folderze na widocznym screenie.
`django-admin.exe startproject mysite .`
![Opis obrazu](katalogi.png)


- Aby utworzyć bazę danych dla naszego bloga, wykonałam następujące polecenie w konsoli
`python manage.py migrate`
![Opis obrazu](migracja.png)

- Uruchomienie strony WWW w konsoli za pomocą:
`python manage.py runserver`
Następnie wpisanie adresu w przeglądarkę: http://127.0.0.1:8000/ 
![Opis obrazu](strona.png)


- Tworzenie osobnej aplikacji wewnątrz naszego projektu, aby utrzymać porządek
`python manage.py startapp blog` 
![Opis obrazu](aplikacja.png)


- Dodanie naszego nowego modelu do bazy danych
`python manage.py makemigrations blog`


- Django przygotował dla nas plik z migracjami, które musimy zastosować teraz do naszej bazy danych. 
Wpisałam: `python manage.py migrate blog` a wynik wygląda tak:
![Opis obrazu](plik_migracje.png)


- W celu dodawania, edycji czy usuwania artykułów, dla których model przed chwilą stworzyłyśmy, użyjemy admina Django.
Po zmianie kodu tak jak jest to opisane w tutorialu oraz wpisaniu
`python manage.py runserver` przeszłam do przeglądarki http://127.0.0.1:8000/admin/ - wyświetli się formularz do zalogowania.


- Wpisuje w do wiersza `python manage.py createsuperuser`, następnie ustawiam nazwe użytkownika, maila itp. oraz loguje się do adminia
![Opis obrazu](admin.png)

- Tworzenie repozytorium Git `git init` oraz `git config --global user.name "Twoja Nazwa Uzytkownika"` i `git config --global user.email ty@adres.pl`

- Utworzenie pliku .gitignore i dodanie treści
`*.pyc
*~
__pycache__
env_dzuls
db.sqlite3
/static
.DS_Store`


- Sprawdzenie zawartości, informację o wszystkich nieśledzonych/zmienionych/zaplanowanych do najbliższego commita plików, statusie brancha 
za pomocą `git status` : 
![Opis obrazu](status.png)

- Zapisanie zmian za pomocą `git add --all` oraz `git commit -m "My Django Girls app, first commit"`
- Mój kod znajduję się już na GitHubie.
- ### Wdrożenie aplikacji internetowej w PythonAnywhere
`pip3.6 install --user pythonanywhere` w konsoli Bash, następnie 
`pa_autoconfigure_django.py https://github.com/kleinszmidt/Integracja_systemow.git`

- Zainicjowanie konta administratora- PythonAnywhere 
`(dzuls.pythonanywhere.com) $ python manage.py createsuperuser`
Sprawdzam swój kod za pomocą `ls` i wygląda następująco:
![Opis obrazu](PythonAnywhere.png)

- Moja strona jest dostępna pod adresem: https://dzuls.pythonanywhere.com/


- Zaimportowanie URL-e z naszej aplikacji blog do głównego pliku mysite/urls.py.
- Stworzenie nowego pustego pliku urlsy.py o treści: 
```from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

- Utworzenie view zgodnie z sugestiami komentarzy
`def post_list(request):
    return render(request, 'blog/post_list.html', {})`
Po zapisaniu pliku i przejściu na adres:  http://127.0.0.1:8000/ wygląda tak: 

![Opis obrazu](widok.png)

- Utworzenie pliku z szablonem oraz wypełnienie go treścią:
<html>
<body>
    <p>Hi there!</p>
    <p>It works!</p>
</body>
</html> 

- Dostosowywanie szablonu: 
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <div>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My first post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        </div>
        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My second post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
        </div>
    </body>
</html>

I widok strony jest następujący: 
![Opis obrazu](html.png)

- Zapisanie zmian w historii i wrzucenie na GitHuba
- Przesłanie nowej wersji kodu na PythonAnywhere i ponowne załadowanie strony
wpisanie w terminalu Bash `cd ~/dzuls.pythonanywhere.com`
i `git pull` wygląda tak: 
![Opis obrazu](dzuls.png)

- W konsoli Django wpisanie polecenia `python manage.py shell`- przejście do 
interaktywnej konsoli Django
- Na początek spróbujmy wyświetlić wszystkie nasze wpisy- następującym poleceniem:
`>>> Post.objects.all()` następnie importujemy "Post" 
`from blog.models import Post` importujemy model Post z blog.models
`Post.objects.all()` lista wpisów wygląda następująco: 
![Opis obrazu](wpisy.png)
- Tworzymy nowy obiekt Post w bazie danych: 
`Post.objects.create(author=me, title='Sample title', text='Test')`, 
ale musimy zaimportować `>>> from django.contrib.auth.models import User`
sprawdzamy jakich użytkowników mamy w bazie `>>> User.objects.all()`
tak to wygląda razem z nowym postem na liście:
![Opis obrazu](obiekt.png)
- W szablonie blog/templates/blog/post_list.html- wpisujemy w body następujący kod:
```
<div>
    <h1><a href="/">Django Girls Blog</a></h1>
</div>

{% for post in posts %}
    <div>
        <p>published: {{ post.published_date }}</p>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endfor %} 
```
![Opis obrazu](szablonu.png)

- 

