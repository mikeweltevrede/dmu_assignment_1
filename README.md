# Decision Making Under Uncertainty

Installing this repository and setting it up for development:

- Open a terminal in the folder where you want to have this repository.
- Clone this repository to your local system: `git clone <enter Github HTTPS here>`
- Move to the repository folder in the terminal: `cd dmu_assignment_1`
- Run `python3 -m venv env`
  - This creates a virtual environment (`venv`) with the name `env`. This makes sure that the packages you install for this project are used only in this project. However, make sure to follow the next steps when doing so.
    - For more information on virtual environments, check this: https://docs.python.org/3/library/venv.html.
  - This will only work if you did not uncheck "Add python.exe to Path" in the installation of Python.
- Activate the virtual environment. There are several options on what you should type in your terminal depending on which terminal you are using:
  - bash/zsh: `source env/bin/activate` (tip on Windows: look into WSL)
  - fish: `source env/bin/activate.fish`
  - csh/tcsh: `source env/bin/activate.csh`
  - Windows Command Prompt: `env\Scripts\activate.bat`
  - Windows Powershell: `env\Scripts\Activate.ps1`
- You should now see `(env)` at the beginning of the newest line to indicate that the virtual environment is activated. Every package you will now install, will be installed only in this virtual environment.
- Install all packages as listed in `requirements.txt` by running `pip3 install -r requirements.txt`. If this gives you an error regarding permissions, run `python3 -m pip3 install -r requirements.txt`.
  - If you want to install a certain package only, for example `numpy`, you can run `pip3 install numpy` instead.
