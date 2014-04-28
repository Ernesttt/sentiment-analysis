Sentiment Analysis 
==================

Sentiment analysis is a REST API for opinion mining (also known as sentiment analysis) of spanish comments. It analizes a comment, tweet, post or sentence and determines sentiment polarity such as negative, positive or neutral according to the vocabulary used. With this API you can:

 > - Analize a single comment and obtain sentiment polarity (positive, negative, neutral)
 > - Analize multiple comments and obtain sentiment polarity of each of these comments
 > - For a set of comments retrieve overall-sentiment polarity
 > - For a set of comments retrieve statistics about sentiment orientation
 > - For a set of comments retrieve a bag of words (folksonomy) related to sentiment orientation


Version
----
0.1



Installation
--------------

```sh
download source file from bit bucket [spribo_content/sentiment-analysis]

```

##### Configure Plugins. Instructions in following README.md files

* plugins/dropbox/README.md
* plugins/github/README.md
* plugins/googledrive/README.md

```sh
node app
```

Usage
-----------

Actually this API support two methods: GET and POST.

###GET:
<p>
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
<enter>
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
          "response": "full"
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
         "full" full response, comment by comment polarity, overall_sentiment, statistics, and folksonomies
         "partial" partial response, ids_only polarity,  overall_sentiment, statistics, and folksonomies
         "minimal" only overall_sentiment and statistics
 

####Data:

- All comments with their respectives id's

Request example:
```sh
curl -X POST http://127.0.0.1:8000/comments -d '{"control": {"classifier": "automatic", "no_classes": "default", "response": "full"}, "data": [{"comment": "primer comentario", "id": 1}, {"comment": "segundo comentario", "id": 2}, {"comment": "n-esimo comentario", "id": 99}]}' -H "Content-Type: application/json"
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

MIT


    