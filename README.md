Sentiment Analysis 
==================

Sentiment analysis is a REST API for opinion mining (also known as sentiment analysis) of spanish comments. It analizes a comment, tweet, post or sentence and determines sentiment polarity such as negative, positive or neutral according to the vocabulary used. With this API you can:

  - Analize a single comment and obtain sentiment polarity (positive, negative, neutral)
  - Analize multiple comments and obtain sentiment polarity of each of these comments
  - For a set of comments retrieve overall-sentiment polarity
  - For a set of comments retrieve statistics about sentiment orientation
  - For a set of comments retrieve a bag of words (folksonomy) related to sentiment orientation


Version
----
0.1.0

Download
--------------

```sh
download source file from bit bucket [spribo_content/sentiment-analysis]
```
 > [sentiment analysis]

###Dependencies:

```sh
python (2.7)
pattern (2.6)
django (1.6.3)
djangorestframework (2.3.13)
django-rest-swagger (0.1.14)
```

Deployment
----------
###Unix-based:
It is highly recommended to use *virtualenv*:
```sh
sudo pip install virtualenv
```
Create the directory for deployment and activate it:
```sh
sudo virtualenv /your_path/deployment_venv
cd /your_path/deployment_venv
source bin/activate
```

Copy sentiment directory into deployment_env directory, project should look like:
```sh
deployment_env
|-- sentiment
|	|-- manage.py
|	|-- tmp.db
|	|-- sentiment
|	|-- comments
|	|	`-- classifier
|	|-- static-files
|	|-- rest-framework-swagger
|-- bin
|-- lib
|-- include
```
Install dependencies:
```sh
pip install pattern
pip install django
pip install djangorestframework
pip install django-rest-swagger
```
####Using GUNICORN for dynamic content:
```sh
pip install gunicorn
cd sentiment
gunicorn sentiment.wsgi:application
```
And now our service is running in http://localhost:8000 or http://127.0.0.1:8000

To chance port use:
```sh
gunicorn sentiment.wsgi:application --bind=127.0.0.1:8001
```
####Using NGINX for static content (pretty browsable interface)

For Linux
```sh
sudo apt-get install nginx
```
For Mac OS, firt install git then homebrew:
```sh
sudo mkdir /usr/local
sudo chown -R `_username_` /usr/local
curl -L http://github.com/mxcl/homebrew/tarball/master | tar xz --strip 1 -C /usr/local
brew install git
cd /usr/local
git init
git remote add origin git://github.com/mxcl/homebrew.git
git pull origin master
```
Then install NGINX:
```sh
brew install nginx
```
Copy the STATIC_ROOT of settings.py (This addres is printed in the bash as /context_address/deployment_env/static-files)
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static-files')
```
Here BASE_DIR is the direction of deployment directory.
Then, modify config nginx file (make backup of config file, just in case)
```sh
cd /usr/local/etc/nginx/nginx.config
```
Modify followig parameters:
```sh
server{
	listen 8000;
	server_name 'your-fully-qualified-domain-name.com';
		
}

location /{
	proxy_pass http://127.0.0.1:8001;
}

location /static/{
	autoindex on;
	alias 'here you put static_root directory'
}

```
To see more options of NGINX configuration see [nginx conf].

Then link config file
```sh
mkdir sites-enabled
sudo ln nginx.config sites-enabled/any_project_name
```
Start servers, first nginx:
```sh
sudo start nginx
```
or:
```sh
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist
```
And run gunicorn as daemon:
```sh
gunicorn sentiment.wsgi:application --bind=127.0.0.1:8001 --daemon
```

###Deploying in Windows with Apache and mod_wsgi:
[Deploying with Apache]
______________________________________
Usage
==============
Actually this API support two methods: GET and POST.

###GET:
URL:
```sh
http://yourdomain.com/comments
```
QUERY_PARAMS
```sh
comment: commet string  (mandatory)
classifier_type: SVM or MNB (optional)
no_classes: 2 or 5 (optional)
```
EXAMPLE_URL : 
```sh
http://localhost:8000/comments?comment=%27este+es+un+comentario+muy+malo%27&classifier_type=MNB&no_classes=2
```
You can also use from bash:
```sh
curl http://localhost:8000/comments?comment=%27este+es+un+buen+comentario%27
```


###POST:

Either in the browser or in bash:
```sh
curl -X POST http://localhost:8000/comments -d 'JSON_FORMAT' -H "Content-Type: application/json"

```
JSON FORMAT:
```sh

{
     "control": {
          "classifier": "automatic", 
          "no_classes": "default", 
          "response": {"folksonomies":true, "comments":"full"}
     }, 
     "data": [
          {
               "comment": "primer comentario", 
               "id": 1
          }, 
          {
               "comment": "segundo comentario", 
               "id": 2
          }, 
          {
               "comment": "n-esimo comentario", 
               "id": 99
          }
     ]
}
```
----------------------------------

We define 2 parts: control and data

#### Control:

- classifier
        "automatic" for automatic selection of classifiers
        "SVM" classifier 88% precision less than 50 words
        "MNB" classifier 77% precision any amount of words
     
- no_classes 
         "default" means 5 classes (muy_negativo, negativo, neutro, positivo, muy_positivo)
         "quick" means 2 classes (negativo, positivo) 

- response
         "folksonomies" if true returns folksonomies (remember json true/false are lowercase)
         "comments"  if "ids_only" returns ids_only polarity, 
                     if "full" returns comment by comment polarity
                     if "nothing" returns nothing

 

####Data:

- All comments with their respectives id's

Request example:
```sh
curl -X POST http://127.0.0.1:8000/comments -d '{"control": {"classifier": "automatic", "no_classes": "default", "response": {"folksonomies":true, "comments":"full"}}, "data": [{"comment": "primer comentario", "id": 1}, {"comment": "segundo comentario", "id": 2}, {"comment": "n-esimo comentario", "id": 99}]}' -H "Content-Type: application/json"
```
Response example:
```sh
{
    "Overall Sentiment": 2.0, 
    "Statistics": {
        "positivos": 0, 
        "neutros": 0, 
        "muy_positivos": 3, 
        "muy_negativos": 0, 
        "negativos": 0
    }, 
    "Comments": [
        {
            "comment": "primer comentario", 
            "polarity": "muy_positivo", 
            "id": 1, 
            "ranking": 5
        }, 
        {
            "comment": "segundo comentario", 
            "polarity": "muy_positivo", 
            "id": 2, 
            "ranking": 5
        }, 
        {
            "comment": "n-esimo comentario", 
            "polarity": "muy_positivo", 
            "id": 99, 
            "ranking": 5
        }
    ], 
    "folksonomies": [
        {
            "muy_negativos": {}
        }, 
        {
            "negativos": {}
        }, 
        {
            "neutros": {}
        }, 
        {
            "positivos": {}
        }, 
        {
            "muy_positivos": {
                "n-esimo comentario": 1, 
                "comentario": 3, 
                "n-esimo": 1
            }
        }
    ]
}
```

License
--------

[BSD]

[sentiment analysis]:https://bitbucket.org/spribo_contenido/sentiment-analysis/get/2f4abb4a945e.zip
[Deploying with Apache]:https://docs.djangoproject.com/en/1.2/howto/deployment/modwsgi/
[BSD]:http://www.linfo.org/bsdlicense.html
[nginx conf]:http://nginx.com/resources/admin-guide/web-server/