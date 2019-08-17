import math

def radian(degree):
    return degree * math.pi / 180 

def declination(day):
    delta = 23.45*math.sin(360*(284+day)/365)
    return radian(delta)

def hourangle(hour, minute, tzmeridian, lmeridian, E):
    w = 15*(hour - 12) + (minute + E)/4 +(tzmeridian - lmeridian)
    return radian(w)

def solarvector(declination, hourangle):
    r = (math.cos(declination)*math.sin(hourangle), math.cos(declination)*math.cos(hourangle), math.sin(declination))
    return r

def sunset(declination, latitude):
    wn = math.acos(-1*math.tan(declination)*math.tan(latitude))
    return wn

def sunrise(declination, latitude):
    wn = -1 * math.acos(-1*math.tan(declination)*math.tan(latitude))
    return wn

def solarheight(declination, hourangle, latitude):
    a = math.asin(math.cos(declination)*math.cos(hourangle)*math.cos(latitude) + math.sin(declination)*math.sin(latitude))
    return a

def localsolarvector(declination, hourangle, latitude):
    r = (math.cos(declination)*math.sin(hourangle), math.cos(declination)*math.cos(hourangle)*math.sin(latitude) - math.sin(declination)*math.cos(latitude),
     math.cos(declination)*math.cos(hourangle)*math.cos(latitude) + math.sin(declination)*math.sin(latitude))
    return r

def solarazimuth(declination, hourangle, latitude, solarheight):
    if hourangle == 0:
        y = math.acos((math.cos(declination)*math.sin(latitude) - math.sin(declination)*math.cos(latitude))/math.cos(solarheight))
    else:
        y = math.acos((math.cos(declination)*math.cos(hourangle)*math.sin(latitude) - math.sin(declination)*math.cos(latitude))/math.cos(solarheight))*(hourangle/abs(hourangle))
    return y

def main():
    day = 228 #int(input("Day: ")) # Day number of the year
    hour = 18 #int(input("Hour: ")) # The time zone standard meridian
    minute = 30 #int(input("Minute: "))
    tzmeridian = 45 #float(input("Time zone meridian: "))
    lmeridian = 37.5 #float(input("Local meridian: "))
    latitude = 55.7 #float(input("Latitude: "))
    B = radian(360*(day - 1)/365)
    E = 229.2*(0.000075 + 0.001868*math.cos(B) - 0.032077*math.sin(B) - 0.014615*math.cos(2*B) - 0.04089*math.sin(2*B))
    DELTA = declination(day)
    HA = hourangle(hour, minute, tzmeridian, lmeridian, E)
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


if __name__ == "__main__":
    main()