# NH_Income_Automation
[Ninja Heroes: New Era](https://www.ninjaheroesnewera.com/)'s Ninja Income Automation Script<br/>
Script to claim Ninja Income for those who have many accounts

## Preparation:
* Install [Python](https://www.python.org/downloads/) 3.8+
* Place your accounts detail in `data.json`
* Install the packages needed by typing `pip install -r requirements.txt` on terminal
* (nh_claim.py: Optional) you can set the value of `BROWSER` variable inside `nh_claim.py` with either `chrome`, `edge` or `firefox` to make it easier later to run the script with just `nh_claim.py` or just run the script directly

## `nh_claim.py`
~~Currently~~ Will only supporting `Chrome`, `Edge`, and `Firefox` and only on `Windows` presumably
The script will run on your browser's private/incognito mode, except for `Firefox`

To run:
1. Open `Windows Explorer` or just skip to step `5`
2. Get into current directory of `nh_claim.py`
3. Press `f4` button
4. Type `cmd`
5. Run the script by typing `nh_claim.py` followed by any browser listed above as an argument e.g. `nh_claim.py edge` then `enter`
6. If the driver is not there yet, it will download the proper driver executable of the selected browser and store it inside `driver\`. Just wait until it's done downloading
7. When the browser window showed, go get your coffee

## `nh_claim-fast.py`
It's the same with `nh_claim.py` but this uses `POST`/`GET` requests to claim the `Ninja Income`, and significantly more efficient than `nh_claim.py`

To run:
1. Basically the same as `nh_claim.py`'s `1 - 4` instruction above
2. Run the script by typing `nh_claim-fast.py` followed by starting point e.g. `nh_claim-fast.py 1` then `enter`
3. Go get your coffee

## Tips:
* When running `Python` script, you can put optional arguments in front of the command with `py` or whatever python executable set-up in the path e.g. `py nh_claim.py`