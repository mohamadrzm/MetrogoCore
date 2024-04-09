![Example Image](logo-github.png)

## ❓ what is Metrogo API ?

This is the core of the Metrogo service. It is written in Python language and Flask framework and uses Dijkstra's algorithm to find the best path.
c
## 🚀 Quick start :

First, install the prerequisites with the following command :
```bash
pip install -r requirements. txt 
```
> [!NOTE]  
> The metrogo api depends on the flask mini-framework and the dijkstar library.

After installing the prerequisites and to run the server, **if you have Windows**, run :
```
win-server.bat
```
and if you have a Linux operating system such as **Linux and Mac OS**, run :
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
"lang":"API input and output language"
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

🎂 Do you want to use Metrogo API in React? Follow this link. [Rendering Lists](https://react.dev/learn/rendering-lists)