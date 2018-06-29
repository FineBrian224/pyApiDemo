import requests

googleApiKey = ''

# # Requests

# response = requests.get('http://httpbin.org/ip')
# print("get ip status: ", response.status_code)
# print(response.content)

# response = requests.post('http://httpbin.org/post')
# print("post status: ", response.status_code)
# print(response.content)

# response = requests.put('http://httpbin.org/put')
# print("put status: ", response.status_code)
# print(response.content)

# # passing params

# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.get('http://httpbin.org/get', params=payload)
# print("get w/ params status: ", response.status_code)
# print(response.content)
# print(response.url)


output = 'json' # options are json or xml

urlFindPlaceFromText = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/'
urlNearbySearch = 'https://maps.googleapis.com/maps/api/place/nearbysearch/'
urlGeocode = 'https://maps.googleapis.com/maps/api/geocode/'
urlDetails = 'https://maps.googleapis.com/maps/api/place/details/'

# payload = {
#     'key': googleApiKey,
#     'inputtype':'textquery',
#     'input': 'Museum of Contemporary Art Australia',
#     'fields': "photos,formatted_address,name,rating,opening_hours,geometry"
# }
# response = requests.get(urlFindPlaceFromText+output, params=payload)
# print("get w/ params status: ", response.status_code)
# print(response.content)
# print(response.url)

payload = {
    'key': googleApiKey,
    'address': '2050 Sugarloaf Circle, Duluth, GA 30097'
}
try:
    response = requests.get(urlGeocode+output, params=payload)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
    SystemExit(1)

print("get geocode status: ", response.status_code)
#print(response.content)
#print(response.url)

responseJson = response.json()

resultsJsonList = responseJson['results']
resultsJsonDict = resultsJsonList[0]

latitude = resultsJsonDict['geometry']['location']['lat']
longitude = resultsJsonDict['geometry']['location']['lng']
placeId = resultsJsonDict['place_id']
formattedAddress = resultsJsonDict['formatted_address']

payload = {
    'key': googleApiKey,
    'placeid': placeId,
    #'fields': 'name,formatted_phone_number'
}
try:
    response = requests.get(urlDetails+output, params=payload)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
    SystemExit(1)

print("get details params status: ", response.status_code)
print('details url:', response.url)
responseJson = response.json()
resultsJson = responseJson['result']
#print(resultsJson['formatted_phone_number'])



# payload = {
#     'key': googleApiKey,
#     'location': str(latitude) + ',' + str(longitude),
#     'radius': 10
# }
# try:
#     response = requests.get(urlNearbySearch+output, params=payload)
# except requests.exceptions.RequestException as e:  # This is the correct syntax
#     print(e)
#     SystemExit(1)

print('adr:', formattedAddress)
print('lat:', latitude)
print('lng:', longitude)
print('place_id:', placeId)
