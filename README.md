# nginx-config
The aim of this repository is to deploy your flask website using Gunicorn and Nginx. The app will be deployed in the most basic settings and you may change the Nginx and Gunicorn configurations by yourself. 
## prerequisites:
* A django application that you have already cloned onto your linux machine.
* A domian mapped to the IP Address of your Linux machine that you wish to use to access your web app.
* A virtual environment enabled.
## Execution:
* Clone this repository inside of the main project directory.
* Activate your virtual environment
* Run the following command:
```
bash nginx-config/nginx-config.sh
```
You may have to enter 'Y' at some points.
You will be asked for the name of the virtual environment, make sure you enter it exactly as it is.
Then you will have to enter the domain that you want to use to display the Webapp.

Wait for a few seconds and Done! You have a deployed flask app.
Go to the your domain in your browser and you can see your webapp.
