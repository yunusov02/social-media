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
