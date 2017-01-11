###################################################################
#                    Scrape Complete, distance matrix google api
###################################################################

import urllib
import simplejson
import ssl


class matrixmaker():
    def __init__(self,locations):
        self.locations = locations
    def matrix(self):
        ssl._create_default_https_context = ssl._create_unverified_context
	YOUR_API_KEY= "PLEASE PLACE YOUR GOOGLE API KEY HERE"
        loc = "Vancouver+BC|Seattle|San+Francisco|Victoria+BC"
        loc = self.locations
        urlstring = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+loc+"&destinations="+loc+"&key="+YOUR_API_KEY
        c = urlstring[0:len(urlstring)-12] +myapikey
	print c

        a = simplejson.load(urllib.urlopen(c))
	print a
        times = []
        distances = []
        origins = []
        destinations = []

        for i in a:
            if i == 'origin_addresses':
                for i in a[i]:
                    origins.append(i)
            if i == 'destination_addresses':
                for i in a[i]:
                    destinations.append(i)
            if i == "rows":
                rows = a[i]
                for i in rows:
                    elements = i
                    for i in elements:
                        duration = elements[i]
                        for i in duration:
                            distance = i
                            for i in distance:
                                if i == "distance":
                                    distances.append(distance[i])
                                if i == "duration":
                                    times.append(distance[i])
        distancedic = {}
        timedic = {}
        alldest = len(origins)
        routinglist = []
        #origin1->dest1->dest2 origin hold
        for i in range(0,len(origins),1):
            for j in range(0,len(destinations),1):
                routinglist.append(origins[i] + '!!!' + destinations[j])
        count = 0

        #goal place1:{place1:0},{place2:4}
        #distancematrix formater
        incompletedistancematrix = {}
        for i in distances:
            routes = routinglist[count]
            origin = str(routes.split('!!!')[0])
            destination = str(routes.split('!!!')[1])
            distance = i['value']
            if origin not in incompletedistancematrix.keys():
                incompletedistancematrix[origin]={destination:distance}
            else:
                incompletedistancematrix[origin][destination]=distance
            count+=1
        IDC = incompletedistancematrix
        distancematrix = IDC
        return distancematrix

if __name__ == "__main__":
	distancematrix = matrixmaker("38.8883,-77.076|38.8122,-77.0545|38.7313,-77.0568|38.8845,-77.1182|38.808,-77.0631|38.8169,-77.0416|38.8355,-77.053|38.8005,-77.0459|38.8341,-77.092|38.8203,-77.053").matrix()
	
