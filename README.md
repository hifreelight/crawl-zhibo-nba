```
scrapy crawl zhibo
```

request
```
{
    category: 'nba'
}
```

response

```js
[
    {
        'category': 'nba',
        'title': 'NBA常规赛 火箭 vs 篮网',
        'time': '', // 比赛时间
        'vs': [
            {
                'name': '火箭',
                'img': '',
                'score': 88,
            },
            {
                'name': '篮网',
                'img':'',
                'score': 78,
            },
        ],
    }
]
```

```js
[
    {
        'eventId': 140354,
        'category': 'nba',
        'title': 'NBA常规赛 火箭 vs 篮网',
        'time': '2018-11-05 20:00', // 比赛时间
        'name1': '火箭',
        'img1': '',
        'score1': 88,
        'name2': '篮网',
        'img2': '',
        'score2': 78,
    }
]
```

https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html

https://fomosports.me/nba-18-19
https://www.zhibo8.cc/
https://bifen4pc.qiumibao.com/json/list_code.htm?77174

https://bifen4pc.qiumibao.com/json/list_code.htm
https://bifen4pc.qiumibao.com/json/list.htm?86205