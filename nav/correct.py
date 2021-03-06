from math import sin
from math import cos
from math import radians
from math import asin
from math import acos
from math import pi

def correct(values = None):
    
    def validate(arg, lowerBound, upperBound, condition):
        if ('d' not in values[arg]):
            return False
        x, y = values[arg].split('d')
        if (x == ''):
            return False
        x = x.lstrip('0')
        if (x == ''):
            x = '0'
        y = y.lstrip('0')
        if (y == ''):
            y = '0'       
        try:
            y = int(y)
        except ValueError:  
            pass     
        else:
            return False
        try:
            if (condition == 'ge'):    
                if (int(x) < lowerBound or int(x) >= upperBound or float(y) < 0.0 or float(y) >= 60.0):
                    return False  
            if (condition == 'gt'):
                if (int(x) <= lowerBound or int(x) >= upperBound or float(y) < 0.0 or float(y) >= 60.0):
                    return False
        except ValueError:
            return False 
                
        y = str(float(y)).zfill(1) 
        values[arg] = x + 'd' + y
        return True
#validate parameters
    if (not(values.has_key('lat')) or values['lat'] == ''):
        values['error'] = 'mandatory information is missing'
        return values   
    if (validate('lat', -90, 90, 'gt') == False):
        values['error'] = 'lat is not valid'
        return values
    
    if (not(values.has_key('long')) or values['long'] == ''):
        values['error'] = 'mandatory information is missing'
        return values
    if (validate('long', 0, 360, 'ge') == False):
        values['error'] = 'long is not valid'
        return values    
    if (values['long'][0] == "-"):
        values['error'] = 'long is not valid'
        return values
    
    if (not(values.has_key('altitude')) or values['altitude'] == ''):
        values['error'] = 'mandatory information is missing'
        return values
    if (validate('altitude', 0, 90, 'gt') == False):
        values['error'] = 'altitude is not valid'
        return values
    
    if (not(values.has_key('assumedLat')) or values['assumedLat'] == ''):
        values['error'] = 'mandatory information is missing'
        return values
    if (validate('assumedLat', -90, 90, 'gt') == False):
        values['error'] = 'assumedLat is not valid'
        return values
    
    if (not(values.has_key('assumedLong')) or values['assumedLong'] == ''):
        values['error'] = 'mandatory information is missing'
        return values
    if (validate('assumedLong', 0, 360, 'ge') == False):
        values['error'] = 'assumedLong is not valid'
        return values
    if (values['assumedLong'][0] == "-"):
        values['error'] = 'assumedLong is not valid'
        return values
    
    
    
    
    
    
    
    
    
#helper function   

    def convertStrToMinutes(arg):
        x, y = arg.split('d')
        if (int(x) >= 0):
            minutes = int(x) * 60 + float(y)
        else:
            minutes = int(x) * 60 - float(y)
        return minutes  
    
    def convertMinutesToStr(arg):
        if (arg >= 0):
            degree = int(arg / 60)
            minutes = round(arg % 60, 1)
        else:
            degree = int(arg / 60)
            minutes = -(round(arg % -60, 1))   
        string = str(degree) + 'd' + str(minutes)           
        return string
    
    def convertStrToDegrees(arg):
        x, y = arg.split('d')
        if (int(x) >= 0):
            degrees = int(x) + float(y)/60
        else:
            degrees = int(x) - float(y)/60
        return degrees
    
    def myRound(arg):
        temp = abs(arg)
        decimal = temp - int(temp)
        if (decimal < 0.5):
            temp = int(temp)
        else:
            temp = int(temp) + 1
        if (arg < 0):
            temp = -temp
        return temp 
    
    LHA = convertStrToDegrees(values['long']) + convertStrToDegrees(values['assumedLong'])
    intermediateDistance = (sin(radians(convertStrToDegrees(values['lat']))) 
        * sin(radians(convertStrToDegrees(values['assumedLat'])))) + (cos(radians(convertStrToDegrees(values['lat']))) 
        * cos(radians(convertStrToDegrees(values['assumedLat']))) * cos(radians(LHA)))
    
    correctedAltitude = convertMinutesToStr(asin(intermediateDistance)*60*180/pi)
    correctedDistance = int(myRound(convertStrToMinutes(values['altitude']) - convertStrToMinutes(correctedAltitude)))
    
    correctedAzimuth = acos(
        (sin(radians(convertStrToDegrees(values['lat']))) - (sin(radians(convertStrToDegrees(values['assumedLat']))) * intermediateDistance))/
        (cos(radians(convertStrToDegrees(values['assumedLat']))) * cos(asin(intermediateDistance)))    
        )
    correctedAzimuth = convertMinutesToStr(correctedAzimuth*60*180/pi)
    if (correctedDistance < 0):
        correctedDistance = abs(correctedDistance)
        correctedAzimuth = (convertStrToMinutes(correctedAzimuth) + 180*60)%(360*60)
        correctedAzimuth = convertMinutesToStr(correctedAzimuth)
    values['correctedDistance'] = str(correctedDistance)
    values['correctedAzimuth'] = correctedAzimuth
    
    return values 