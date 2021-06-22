from quart import request
import asyncio
import requests
from requests_html import AsyncHTMLSession
from quart import Quart
import json

app = Quart(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def getLocationFromGeo(latitude,longitude,lang):
    urlGeoApi = "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude="+latitude+"&longitude="+longitude+"&localityLanguage="+lang
    r = requests.get(urlGeoApi)
    
    province = r.json()["principalSubdivision"]
    locality = r.json()["locality"]
    country = r.json()["countryName"]

    plusCode = r.json()["plusCode"]
    localityLanguage = r.json()["localityLanguageRequested"]
    continent = r.json()["continent"]
    countryCode = r.json()["countryCode"]
    provinceCode = r.json()["principalSubdivisionCode"]
    postcode = r.json()["postcode"]

    ar = [province,locality,country,plusCode,localityLanguage,continent,countryCode,provinceCode,postcode]
    return(ar)

def getJsonCurrentWeather(pluscode,latitude,longitude,country,province,
locality,fullName,localityLanguage,continent,provinceCode,countryCode,postcode,
time,fahrenheit,celsius,weatherEvent,precipitation,humidity,wind):

    str = '{"geoLocation":[{"plusCode":"'+pluscode+'"},{"latitude":"'+latitude+'","longitude":"'+longitude+'"}],"country":"'+country+'","province":"'+province+'","locality":"'+locality+'","fullName":"'+fullName+'","localityLanguage":"'+localityLanguage+'","continent":"'+continent+'","provinceCode":"'+provinceCode+'","countryCode":"'+countryCode+'","postcode":"'+postcode+'","weather":[{"Time":"'+time+'","fahrenheit":"'+fahrenheit+'","celsius":"'+celsius+'","weatherEvent":"'+weatherEvent+'","precipitation":"'+precipitation+'","humidity":"'+humidity+'","wind":"'+wind+'"}]}'
    json_object = json.loads(str)
    json_formatted_str = json.dumps(json_object, indent=2)
    return(json_formatted_str)


@app.route('/current', methods=['GET'])
async def geo_location():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    lang = request.args.get('lang')
    
    asyncio.set_event_loop(asyncio.new_event_loop())
    session = AsyncHTMLSession()
    ar = getLocationFromGeo(lat,lon,lang)
    searchElement = ar[0]+"+"+ar[1]+"+"+ar[2]
    searchElement = searchElement.replace(" ","+")
    print(searchElement)
    urlWeather = "https://www.google.com/search?hl="+lang+"&as_q=&as_epq="+searchElement+"+weather&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=lang_en&cr=&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs="
    r = await session.get(urlWeather)
    await r.html.arender(sleep = 0.5,keep_page= True,scrolldown = 1)

    celsius = r.html.xpath("//*[@id='wob_tm']/text()")[0]
    fahrenheit = r.html.xpath("//*[@id='wob_ttm']/text()")[0]
    fullName = r.html.xpath("//*[@id='wob_loc']/text()")[0]
    time = r.html.xpath("//*[@id='wob_dts']/text()")[0]
    weatherEvent = r.html.xpath("//*[@id='wob_dc']/text()")[0]
    precipitation = r.html.xpath("//*[@id='wob_pp']/text()")[0]
    humidity = r.html.xpath("//*[@id='wob_hm']/text()")[0]
    wind = r.html.xpath("//*[@id='wob_ws']/text()")[0]
    

    result = getJsonCurrentWeather(str(ar[3]),str(lat),str(lon),str(ar[2]),str(ar[0]),str(ar[1]),str(fullName),str(ar[4]),str(ar[5]),str(ar[7]),str(ar[6]),str(ar[8]),str(time),str(fahrenheit),str(celsius),str(weatherEvent),str(precipitation),str(humidity),str(wind))
    return result

if __name__ == '__main__':
    app.run(port=8080)

