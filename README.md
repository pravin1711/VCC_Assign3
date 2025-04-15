# TransCloud Travel Optimizer.

Step 1: Create a virtual machine
Step 2: Run that machine
Step 3: create an environment to run all the files .
Step 4: Install the necessary dependencies, like(Google authentication, flask, psutil, python etc.).
Step  5: Activate the environment.
Step 6: create three py file.
•	one is app.py which is basically containing printing statement using flask.
•	Monitor.py for monitoring the usage og resources(CPU).
•	Deploy.py for deploying the app.py on Google ccloudwhen the resource usage is exceeding 75%.
Step 6: After doing all the authentication to connect to google cloud.
Step 7: Run app.py and monitor.py, when resource usage crosses a threshold. It run the deploy.py file which is doing the deployment on the google cloud.
Step 8: On google cloud a vm is created with specified configuration is created where app.py is deployed.

