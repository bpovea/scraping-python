# Python - Scrapy, Stackoverflow

## how to install dependences (pip):
> pip install -r requirements.txt

## how to run:
> scrapy runspider [file_name].py -o [output-file_name].csv -a tab=[tab_name]

-a tab=[tab_name] is an optional attribute

ex: scrapy runspider spider.py -o preguntas.csv
ex2: scrapy runspider spider.py -o preguntas.csv -a tab=hot

## documentation:
- [Scrapy](https://doc.scrapy.org/en/latest/topics/spiders.html) 
- [Video tutorials - Web Scraping Python, Leonardo Kuffo](https://www.youtube.com/watch?v=ViOFqeRgu5s&t=0s)