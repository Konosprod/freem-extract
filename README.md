# Freem-extract

Extract data from Freem!. Main purpose is to create entries on VNDB. The program uses [cutlet](https://github.com/polm/cutlet) to translate original titles into romaji following the hepburn system. There is no Wapuro system support in python AFAIK. 

### Data format

The program will generate JSON with the following structure :

```json
[
  {
    "title": {
      "original": "薔薇と蛇の冑",
      "romaji": "Bara to hebi no kabuto"
    },
    "os": [
      "Windows",
      "Browser"
    ],
    "rating": "AGE 15+",
    "date": "2021-10-21",
    "author": {
      "original": "紫",
      "romaji": "Murasaki"
    },
    "url": "https://www.freem.ne.jp/win/game/26893"
  }
]
```
### Requirements

* [requests](https://github.com/psf/requests)
* [cutlet](https://github.com/polm/cutlet)
