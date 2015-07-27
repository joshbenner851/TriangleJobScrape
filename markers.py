#googlemaps
from googlemaps import Client

'''All I want to be able to do is something like the javascript example:
url to that page https://developers.google.com/maps/documentation/javascript/examples/marker-simple


function initialize() {
  var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
  var mapOptions = {
    zoom: 4,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Hello World!'
  });
}

google.maps.event.addDomListener(window, 'load', initialize);

'''

c = Client(key="XXXXXXX")

d = c.directions("texarkana","atlanta")
steps = c.directions("texarkana","atlanta")[0]["legs"][0]["steps"]

for d in steps:
    print(d['html_instructions'])
