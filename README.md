# NH_Income_Automation
[Ninja Heroes: New Era](https://www.ninjaheroesnewera.com/)'s Ninja Income Automation Script

Script to claim Ninja Income for those who have many accounts
~~Currently~~ Will only supporting `Chrome`, `Edge`, and `Firefox` on `Windows` only presumably
The script will run on your browser's private/incognito mode, except for `Firefox`

Preparation:
* Install [Python](https://www.python.org/downloads/) 3.8+
* Place your accounts detail in `data.json`
* Install the packages needed by typing `pip install -r requirements.txt` on terminal
* (Optional) you can set the value of `BROWSER` variable inside `nh_claim.py` with either `chrome`, `edge` or `firefox` to make it easier later to run the script with just `nh_claim.py`

To run:
1. Open `Windows Explorer` or just skip to step `5`
2. Get into current directory of `nh_claim.py`
3. Press `f4` button
4. Type `cmd`
5. Run the script by typing `nh_claim.py` followed by any browser listed above as an argument e.g. `nh_claim.py edge` then `enter`
6. If the driver is not there yet, it will download the proper driver executable of the selected browser and store it inside `driver\`. Just wait until it's done downloading
7. When the browser window showed, go get your coffee

Note:
* When running the script if the argument after the script file name is not passed or simply wrong then it will use the value inside `BROWSER` variable
* When running `Python` script, you can put optional arguments in front of the command with `py` or whatever python executable set-up in the path e.g. `py nh_claim.py`