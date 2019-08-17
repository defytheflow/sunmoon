import math

def declination(day):
    delta = 23.45*sin(360*(284+day)/365)
    return delta

def hourangle(hour, minute, tzmeridian, lmeridian):
    w = 15*(hour - 12) + (minute + E)/4 +(tzmeridian - lmeridian)
    return w

def solarvector(declination, hourangle):
    r = (cos(declination)*sin(hourangle), cos(declination)*cos(hourangle), sin(declination))
    return r

def sunset(declination, latitude):
    wn = math.arccos(-tan(declination)*tan(latitude))
    return wn

def sunrise(declination, latitude):
    wn = -1 * math.arccos(-tan(declination)*tan(latitude))
    return wn

def solarheight(declination, hourangle, latitude):
    a = math.arcsin(cos(declination)*cos(hourangle)*cos(latitude) + sin(declination)*sin(latitude))
    return a

def localsolarvector(declination, hourangle, latitude):
    r = (cos(declination)*sin(hourangle), cos(declination)*cos(hourangle)*sin(latitude) - sin(declination)*cos(latitude), cos(declination)*cos(hourangle)*cos(latitude) + sin(declination)*sin(latitude))
    return r

def solarazimuth(declination, hourangle, latitude, solarheight):
    if hourangle == 0:
        y = math.arccos((cos(declination)*sin(latitude) - sin(declination)*cos(latitude))/cos(solarheight))
    else
        y = math.arccos((cos(declination)*cos(hourangle)*sin(latitude) - sin(declination)*cos(latitude))/cos(solarheight))*(hourangle/abs(hourangle))
    return y

def main():
    day = input("Day: ") # Day number of the year
    hour = input("Hour: ") # The time zone standard meridian
    minute = input("Minute: ")
    tzmeridian = input("Time zone meridian: ")
    lmeridian = input("Local meridian: ")
    latitude = input("Latitude: ")
    B = 360*(day - 1)/365
    E = 229.2*(0.000075 + 0.001868*math.cos(B) - 0.032077*math.sin(B) - 0.014615*math.cos(2*B) - 0.04089*math.sin(2*B))
    DELTA = declination(day)
    HA = hourangle(hour, minute, tzmeridian, lmeridian)
    SV = solarvector(DELTA, HA)
    SUNSET = sunset(DELTA, latitude)
    SUNRISE = sunrise(DELTA, latitude)
    SH = solarheight(DELTA, HA, latitude)
    LSV = localsolarvector(DELTA, HA, latitude)
    SA = solarazimuth(DELTA, HA, latitude, SH)

    print(f"Sunset today at {SUNSET} degrees")
    print(f"Sunrise today at {SUNRISE} degrees")
    print(f"Sun right now located {SA} and {SH}")
    print(f"Local Solar Vector {LSV}")

    return 0;
