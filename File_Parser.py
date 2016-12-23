#FileParser
class FileParse():
    def __init__(self,linedata):
        self.linedata = linedata
    def latlon(self):
        linedata = self.linedata
        count = 0
        nameandlatlong = {}
        for line in linedata:
            
            if "var point" in line:
                latlong=str(line.split("LatLng")[1])
                latlong = latlong[0:len(latlong)-2]
                nextline = linedata[count+1]
                house_name = nextline.split(',')[2]
                street_address = nextline.split(">")[1]
                apartment = nextline.split(">")[2]
                house_address=street_address[0:len(street_address)-3]
                housecheck = bool
                if apartment[0:3] == "Apt":
                    housecheck = False
                    apartmentnumber = apartment[0:len(apartment)-3]
                    city = nextline.split('>')[3]
                elif apartment[0] == "#":
                    housecheck = False
                    apartmentnumber = apartment[0:len(apartment)-3]
                    city = nextline.split('>')[3]
                else:
                    housecheck = True
                    city = apartment
                    apartmentnumber = None
                city=city[0:len(city)-6]
                nameandlatlong[house_name]=latlong
            count+=1
        namelist = []
        for i in nameandlatlong:
            latlong = nameandlatlong[i]
            lat = latlong.split(',')[0]
            lat = lat[1:len(lat)]
            longitude = latlong.split(',')[1]
            longitude = str(longitude)
            longitude = longitude[0:len(longitude)-1]
            housename = i[1:len(i)-1]
            namelist.append([housename,lat,longitude])
            
        ##print namelist
        def locationformater(namelist):
            locations = ""
            count = 0
            for i in namelist:
                lat = i[1]
                lon = i[2]
                if count < 9:
                    locations += lat + "," +lon +"|"
                elif count < 10:
                    locations += lat + "," +lon
                count +=1
            return locations
        locations = locationformater(namelist)
        return locations
