from math import sin, cos, radians, asin, acos, pi


def correct(values = None):
    def validate(arg, lowerBound, upperBound):
        if ('d' not in values[arg]):
            return False
#validate parameters
    if (not(values.has_key('lat')) or values['lat'] == ''):
        values['error'] = 'mandatory information is missing'
        return values
    
    if (validate('lat', -90, 90) == False):
        values['error'] = 'lat is not valid'


    
#helper function   

        
        
        
        



     
    def convertStrToMinutes(arg):
        x, y = arg.split('d')
        minutes = int(x) * 60 + float(y)
        return minutes  
    def convertMinutesToStr(arg):
        degree = int(arg / 60)
        minutes = round(arg % 60, 1)
        string = str(degree) + 'd' + str(minutes)
        return string
    def convertStrToDegrees(arg):
        x, y = arg.split('d')
        degrees = int(x) + float(y)/60
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