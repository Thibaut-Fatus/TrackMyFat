# TrackMyFat

This should one day allow you to track your nutritional intake after going to McDonald's 

You will be able to see how much sugar, fat and salt your last meal gave you, your weekly / monthly consumption

It could be nice if I find time to add some data-viz on top of this.

USAGE
-----

- You need to set you PYTHONPATH correctly to TrackMyFat

- Install python requirements
```
pip install -r back/requirements.txt
```

- built javascript files:
```
jsx --watch src/ build/
```

- django runserver
```
python manage.py runserver localhost:8888
```

If you want to test the scraper, go to back/scrapy and run:

```
scrapy crawl macdo
```

and you will see current state of parsing
