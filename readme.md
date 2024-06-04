![Example Image](logo-github.png)

## ❓ what is Metrogo API ?

This is the core of the Metrogo service. It is written in Python language and Flask framework and uses Dijkstra's algorithm to find the best path.

## 🚀 Quick start :

First, install the requirements with the following command :
```bash
pip install -r requirements. txt 
```
> [!NOTE]  
> The metrogo api depends on the Fastapi and the dijkstar library.

For Start MetrogoCore in dev mode use this command :
```
fastapi dev server.py
```

🧪 To get the best route, you need to send a POST request in json format with the following values to the api:
```json
{
"source": "Source station",
"dist":"Destination station",
"color": true or false (Optional. default is false)
}
```
> [!TIP]
> Even if you send the names of the origin and destination stations wrongly. It is automatically corrected to the closest match

For Example :
```json
{
"source": "تئاتر شهر",
"dist":"تجریش",
"lang":"farsi"
}
```
The api response will be as follows:

```json
{
    "stations": {
        "تئاتر شهر",
        "میدان حضرت ولیعصر",
        "میدان جهاد",
        "میرزای شیرازی",
        "شهید بهشتی",
        "مصلی امام خمینی",
        "شهید همت",
        "شهید حقانی",
        "دکتر شریعتی",
        "قلهک",
        "شهید صدر",
        "قیطریه",
        "تجریش"
    }
}
```
And another example, this time with color :
```json
{
"source": "تئاتر شهر",
"dist":"تجریش",
"color": true
}
```
The answer will be as follows :
```json
{
    "stations": {
        "تئاتر شهر": "sky",
        "میدان حضرت ولیعصر": "sky",
        "میدان جهاد": "sky",
        "میرزای شیرازی": "sky",
        "شهید بهشتی": "red",
        "مصلی امام خمینی": "red",
        "شهید همت": "red",
        "شهید حقانی": "red",
        "دکتر شریعتی": "red",
        "قلهک": "red",
        "شهید صدر": "red",
        "قیطریه": "red",
        "تجریش": "red"
    }
}
```