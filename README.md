# social-media
Social Media Application with Django and DRF


## At the beginning use pip but later change it to poetry/uv

The First thing we need to start of creating new project using `django-admin`

```shell
django-admin startproject core . # core because nessassary object will live there

```

## Requirements

* User Auth (session, OTP, JWT, telegram based auth login)
* User profiles (name bio avatar)
* Posts CRUD (With multiple images)
* Like Posts
* Basic Comments
* Follow
* Simple Feed (latest posts related posts)
* Bookmark posts

<br>

* News feed Algorithm
* Pagination
* Search (users + posts)
* Notifications (likes, comments follows)
* API optimizations (select_releated, prefetch_related)
* Query optimiations

<br>

* Real-Time chat
* Real-time notifications
* hashtags #search
* mentions @users
* Recommendation system basic
* Media Storage

<br>

* Stories
* Reels & shorts
* Content Moderations
* Blocking users



### Get Django version
```python
import django
print(django.get_version())
```

```shell
python -m djnago --version
```

### manage.py commands

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate app_name 001 # print sql command implemented
python manage.py shell # to go shell
```

`migrate` command looks at the INSTALLED_APPS settings and creates any necessary database tables according to the database 

```shell
# To see all database tables
\dt # PostgreSQL
.tables # SQLite
select table_name from user_tables; # Oracle
```

### Playing with django shell

`modelname_set` or `choice_set` is a reverse relation manager that Django automatically creates on the one side of a Foreign Key relationship

```
<model_name_lowercase>_set
```

```python
# Choice has: question = models.ForeignKey(Question, on_delete=models.CASCADE)
# Django automatically creates: Question.choice_set → manages related Choice objects

q = Question.objects.get(id=1)

# This works ✅ — because choice_set is tied to the Choice model
q.choice_set.create(choice_text='Option A', votes=0)

# This does NOT work ❌ — text is a field on TestModel, not Choice
q.choice_set.create(text='something')
```

### Views is responsible for doing of two things 
* `HttpResponse`
* `Htpp404`


### Use generice views: Less code is better

