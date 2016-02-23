import requests
import requests.exceptions
import json


class NoFlightDataException(Exception):
    pass


class InvalidFormattingException(NoFlightDataException):
    REASON = 'invalid_formatting'


class ConnectionException(NoFlightDataException):
    REASON = 'could_not_connect'


class FlightInfo(object):
    # gogo inflight wil lreturn something like this. At least it did on this one flight..

    """
    {
        "HSpeed": 186.19803, 
        "VSpeed": 0.099609, 
        "abpVersion": "5.0.4", 
        "acpuVersion": "8.2.0", 
        "airlineCode": "ASA", 
        "airlineCodeIata": "AS", 
        "airlineName": "Alaska Airlines", 
        "altitude": 9769.6, 
        "departureAirportCode": "KORD", 
        "departureAirportCodeIata": "ORD", 
        "destination": "SEA", 
        "destinationAirportCode": "KSEA", 
        "destinationAirportCodeIata": "SEA", 
        "expectedArrival": "2016-02-17T06:30:37Z", 
        "flightNumberAlpha": "ASA", 
        "flightNumberInfo": "ASA21", 
        "flightNumberNumeric": 21, 
        "latitude": 47.00781, 
        "localTime": "2016-02-17T05:14:33.0Z0:0", 
        "longitude": -111.97815, 
        "origin": "ORD", 
        "tailNumber": "N435AS", 
        "utcTime": "2016-02-17T05:14:33Z", 
        "videoService": false
    }
    """

    def gogoinflight_metadata(self):
        try:
            m = requests.get('http://airborne.gogoinflight.com/abp/ws/absServices/statusTray')
        except requests.exceptions.RequestException, rqe:
            raise ConnectionException("Request exception %s while querying Gogo Inflight" % rqe.__class__.__name__)

        try:
            flightinfo = json.loads(m.text)
            return flightinfo['Response']['flightInfo']
        except ValueError:
            raise InvalidFormattingException("Invalid formatting on Gogo Inflight response: not JSON")
        except KeyError:
            raise InvalidFormattingException("Response.flightInfo not defined in Gogo Inflight response.")

    # at some point, it would be nice for FlightInfo to be able to figure out which type of flight tracking is available
    # by trying several and abstract it away. For now.. just does gogo. Very simple.
