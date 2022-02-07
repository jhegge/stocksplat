# stocksplat -- Stock quote summary API

Simple web service to wrap a call to a stock quote service, supplying a stock 
symbol and the number of days for quotes. The service returns JSON with the daily 
stock data for those days along with an average close price over those days.

The app is supplied with a Dockerfile to build and run the service.

## Building

The web service runs as a Flask app in a python/alpine image with a requirements.txt file
supplied to setup the image.

The Docker image is built with the following example command line:
`docker build -t stocksplat:1  .`

## Running the docker image

The docker images service is started by setting two environment variables, `SYMBOL` and `NDAYS`,
e.g. `SYMBOL=MSFT` and `NDAYS=6` for the container and exposing the service port. 
These default to `ABC` and `3`.
Additionally, the API key for the quote service is supplied via environment variable as 
`APIKEY`.
The service port is set to 8080. 

An example service startup:

`docker run -d -p 8080:8080 stocksplat:1`

## Running the Kubernetes service

The web service is supplied with a set of Kubernetes YAML manifest files to deploy 
the service (single instance).  A Kubernetes deployment and service are configured 
based on the environment variables supplied by the ConfigMap and Secret. The service
is exposed externally with simple Ingress for an external IP address. 

The five manifest files are required to start the service, as follows:

Change to this repo's source directory and use kubectl to create the deploy.

`cd stocksplat`

`kubectl apply -f k8s/`

The output from minikube would be similar:
```commandline
kubectl apply -f k8s/
configmap/stocksplat-config created
deployment.apps/stocksplat-deployment created
ingress.networking.k8s.io/stocksplat-ingress created
secret/apikey-secret created
service/stocksplat-service created
```