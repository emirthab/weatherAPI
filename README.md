<h1 align="center">Weather API</h1>

<p align="center">
  <a href="https://github.com/emirthab/weatherAPI">
    <img src="https://purepng.com/public/uploads/large/weather-forecast-symbol-v7o.png" alt="Weather API" width="300">
  </a>
</p>
 
## Introduction:

:large_blue_circle: An API that returns weather data in json format based on the geolocation information entered.

## Important Note: 

**❗️In this application, it is not possible to sell, rent or use the data commercially. This application was made for testing purposes. Since it works as a bot, it works slower than apis that sell data.**
**You can use the api in your projects from the following link (see usage section):**

"**https://github.com/emirthab/weatherAPI**(To be added)"

## Usage :

* ### Install requirements:
```
python -m pip install -r requirements.txt
```

* ### Run Application:
```
python listener.py
```
* ### Example Request:
```
127.0.0.1:8080/current?lat=40.12345&lon=35.12345&lang=en

lat = latitude
lon = longitude
lang = language
```
## How It Works:

:large_blue_circle: First, geolocation information is sent to the API via https://bigdatacloud.net, then the location data corresponding to this information is returned in json format.

#### On listener.py/line 11:
```
def getLocationFromGeo(latitude,longitude,lang):
    urlGeoApi = "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude="+latitude+"&longitude="+longitude+"&localityLanguage="+lang
    r = requests.get(urlGeoApi)
```
#### Example Json Data:

<p align="left">
    <img src="https://github.com/emirthab/weatherAPI/blob/main/img/img-1.png?raw=true" alt="Json Example" width="600">
</p>

:large_blue_circle: The **full address name** is created in the following data.
For example:
```
city: "Mountain View"
locality: "Googleplex"
countryName: "USA"
```
for this data:
**'Mountain View Googleplex USA'**

the full address name is obtained.


:large_blue_circle: Then the word **"weather"** is added to the end of this address and only **"weather widget"** is displayed in the **Google search engine**.

#### Example Google Search:

<p align="left">
    <img src="https://github.com/emirthab/weatherAPI/blob/main/img/img-2.png?raw=true" alt="Google Search Example" width="600">
</p>

:large_blue_circle: As seen in the image above, a special search was made on Google to show **only the weather widget**.
After this search is done, all the data obtained by taking the html data according to **"xpath"** is returned in a json format.

**NOTE: The extraction of html data with Xpath took place between lines 55 and 62.**

#### :large_blue_circle: The resulting json data will look like this:

<p align="left">
    <img src="https://github.com/emirthab/weatherAPI/blob/main/img/img-3.png?raw=true" alt="Result Json Data" width="600">
</p>
