# func-app
Azure function app using Python

## To install dependencies:
`pipenv shell`
`pipenv install`

## To run the app on local:
1. Make sure you have Azure CLI installed on your machine: Refer following link : https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
1. Make sure you have azure function core tools install in your local machine. Refer to the link to install it on your local machine : https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash
2. Once tool is successully install then run:
  %`func host start` (add --verbose in case you see issues and it can help to debug)

## Push the app to Azure cloud:
Run command: `func azure functionapp publish <APP_NAME>`

