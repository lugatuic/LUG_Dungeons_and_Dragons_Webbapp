VENV
To install venv enter the following command:

$ python3 -m venv venv

This installs the venv package and names the folder "venv".


To activate the VM, navigate to the directory where your venv folder is located.

For linux users:
$ source venv/bin/activate

For windows users using cmd:
$ venv\Scripts\activate


To get out of the VM:
$ deactivate


DEBUGGING
If the debugger does not activate while testing app, use the following flag to constantly update page without needing to restart the server:

$ export FLASK_DEBUG=1
