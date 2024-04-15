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

