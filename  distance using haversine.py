import math 

radius_e = 6378137
radius_p = 6356752

Latitude_User = float(input('Enter the latitude of the location in degrees'))
Longitude_User = float(input('Enter the longitude of the location in degrees'))

a = math.sin((0.89035807582-math.radians(Latitude_User))/2)**2 + math.cos(0.89035807582) * math.cos(math.radians(Latitude_User)) * math.sin((1.992008695399-math.radians(Longitude_User))/2)**2

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

R = 1/3 * (2 * radius_e + radius_p)

Dist = (R * c)/1000

i_1 = (Latitude_User)*3600/60
degrees_Lat = round(i_1/60)
minutes_Lat = round(i_1%60)
seconds_Lat = round((Latitude_User)*3600%60,2)

i_2 = (Longitude_User)*3600/60
degrees_Long = round(i_2/60)
minutes_Long = round(i_2%60)
seconds_Long = round((Longitude_User)*3600%60,2)

print('The Homage Location : 51\u00B0 0\' 49.54\'\', 114\u00B0 8\' 1.29\'\'','and','Your location :',degrees_Lat,'\u00B0',minutes_Lat,'\'',seconds_Lat,'\'\'',',',degrees_Long,'\u00B0',minutes_Long,'\'',seconds_Long,'\'\'') 
print(f'The distance between The Homage and your desired location is {Dist:.1f} km')


#For the degree symbol, credit goes to https://theprogrammingexpert.com/python-degree-symbol/#:~:text=In%20Python%2C%20to%20print%20the,degree%20sign%20'%5Cu00B0'
#For getting a start on converting decimal degrees to DMS format, credit goes to https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.inchcalculator.com%2Fconvert-degrees-to-degrees-minutes-seconds%2F&psig=AOvVaw3_sSJz11ZdH8Vs7AyC7e-3&ust=1665220504459000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCODps_fjzfoCFQAAAAAdAAAAABAD 
