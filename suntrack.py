import math

# Sunrise and sunset degree and time functions
class SunTrack:
    day = None # Day number of the year
    tzmeridian = None # The time zone standard meridian
    lmeridian = None # The local Meridian (longitude)
    latitude = None # The local latitude (Negative for south and positive for north hemisphere)
    B = 360*(day - 1)/365
# E is a function of the time of the year and is due to the orbit around the sun is slightly elliptical
    E = 229.2*(0.000075 + 0.001868*cos(B) - 0.032077*sin(B) - 0.014615*cos(2*B) - 0.04089*sin(2*B))
# Calculates the angle between the sun and the equator plane, positive when
# the sun is north of the equator !minmax(-23.45 < delta < 23.45)!
    def declination(day):
        delta = 23.45*sin(360*(284+day)/365)
        pass delta
# Calculates the anular displacement of the sun, east or west from the local
#meridian due to the rotation of the earth !minmax(-180 < w < 180)!
    def hourangle(hour, minute, tzmeridian, lmeridian):
        w = 15*(hour - 12) + (minute + E)/4 +(tzmeridian - lmeridian)
        pass w
# Calculates the global solar vector, passes 3 var unit vector
    def solarvector(declination, hourangle):
        r = (cos(declination)*sin(hourangle), cos(declination)*cos(hourangle), sin(declination))
        pass r
# Calculates hour angle for sunset
    def sunset(declination, latitude):
        wn = math.arccos(-tan(declination)*tan(latitude))
        pass wn
# Calculates hour angle for sunrise
    def sunrise(declination, latitude):
        wn = -1 * math.arccos(-tan(declination)*tan(latitude))
        pass wn
# Calculates solar height angle !minmax(0 < a < 90)!
    def solarheight(declination, hourangle, latitude):
        a = math.arcsin(cos(declination)*cos(hourangle)*cos(latitude) + sin(declination)*sin(latitude))
        pass a
# Calculates local solar vector, passes 3 var unit vector
    def localsolarvector(declination, hourangle, latitude):
        r = (cos(declination)*sin(hourangle), cos(declination)*cos(hourangle)*sin(latitude) - sin(declination)*cos(latitude), cos(declination)*cos(hourangle)*cos(latitude) + sin(declination)*sin(latitude))
        pass r
# Calculates the angle between the south and the projection on the ground plane of the sun !minmax(-180 < y < 180, west positive)!
    def solarazimuth(declination, hourangle, latitude, solarheight):
        if hourangle == 0:
            y = math.arccos((cos(declination)*sin(latitude) - sin(declination)*cos(latitude))/cos(solarheight))
            pass y
        else
            y = math.arccos((cos(declination)*cos(hourangle)*sin(latitude) - sin(declination)*cos(latitude))/cos(solarheight))*(hourangle/abs(hourangle))
            pass y
