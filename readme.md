![Example Image](logo-github.png)

## ❓ what is Metrogo API ?

This is the core of the Metrogo service. It is written in Python language and Flask framework and uses Dijkstra's algorithm to find the best path.

## 🚀 Quick start :

First, install the requirements with the following command :
```bash
pip install -r requirements. txt 
```
> [!NOTE]  
> The metrogo api depends on the flask mini-framework and the dijkstar library.

After installing the requirements and to run the server, **if you have Windows**, run :
```
win-server.bat
```
and if you have a Unix operating system such as **Linux and Mac OS**, run :
```
unix-server.sh
```
> [!NOTE]  
> Metrogo server runs on localhost and port 5000. You can access the Metrogo api by using endpoint /getbestpath.

🧪 To get the best route, you need to send a POST request in json format with the following values to the api:
```json
{
"source": "Source station",
"dist":"Destination station",
"lang":"API input and output language",
"color": true or false #Optional. default is false
}
```
> [!TIP]
> Even if you send the names of the origin and destination stations wrongly. It is automatically corrected to the closest match

The value of lang can be Farsi or English. In this example, it is assumed that you have set the value of lang equal to farsi. We enter the source value as the source station, for example, the city theater, and the dist value as the destination station, for example, Tajrish, and our json is sent to the api as follows:
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
    "stations": [
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
    ],
    "time": 13
}
```
> [!NOTE]  
> **time** sends the arrival time between the origin and destination stations
And another example, this time with color :
```json
{
"source": "تئاتر شهر",
"dist":"تجریش",
"lang":"farsi",
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
    },
    "time": 39
}
```
🎂 Do you want to use Metrogo API in React? Follow this link. [Rendering Lists](https://react.dev/learn/rendering-lists)