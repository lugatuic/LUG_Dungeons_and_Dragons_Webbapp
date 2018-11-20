INSTALL REQUIREMENTS
You can install flask and other requirements such as RESTfulapi for flask by simply running this script:

$ pip install -r requirements.txt

-------------------------
VENV
To install venv enter the following command:

$ python3 -m venv venv

This installs the venv package and names the folder "venv".

To activate the VM, navigate to the directory where your venv folder is located.

For linux users:
$ source venv/bin/activate

For windows users using cmd:
> venv\Scripts\activate

Powershell script:
> venv\Scripts\activate.ps1

Note*: If Powershell gives an execution error, just use cmd or follow this link to see execution policy documentation: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-5.1

To exit out of the VM:
$ deactivate

-------------------------
RUNNING THE APP
In order to run the app, first you have to navigate to the directory the app is stored in. Than you must set an environment variable to the file that we want to be our flask application.
For example, if our application was named DND.py we would input the following flag in the terminal:

For Linux:
$ export FLASK_APP=DND.py

For Windows:
>set FLASK_APP=DND.py

To actually run the application, input the following:
$ flask run
    or
$ python DND.py

If you ran it correctly you should see the following information come up on your terminal:

$ python DND.py
 * Serving Flask app "DND" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 298-103-098

-------------------------
DEBUGGING
If the debugger does not activate while testing app, use the following flag to constantly update page without needing to restart the server:
$ export FLASK_DEBUG=1

-------------------------
ERROR CHECKING
Pylint is a great linter for this project so we will be using that to check for errors or warnings before running.

To lint the app, use the command:

$ pylint app_name.py
