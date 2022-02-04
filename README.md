# stocksplat -- Stock quote summary API

Simple web service to wrap a call to a stock quote service, supplying a stock 
symbol and the number of days for quotes. The service returns JSON with the daily 
stock data for those days along with an average close price over those days.

The app is supplied with a Dockerfile to build and run the service.

## Building

The web service runs as a Flask app, a python image with a requirements.txt file
is supplied to setup the image.

The Docker image is built with the following example command line:
`docker build -t stocksplat:1  .`

## Running

The service is started by setting two environment variables, `SYMBOL` and `NDAYS`,
e.g. `SYMBOL=MSFT` and `NDAYS=6` for the container and exposing the service port.
The port is set to 8080. 

An example service startup:

`docker run -d -p 8080:8080 stocksplat:1`