# NH_Income_Automation
[Ninja Heroes: New Era](https://www.ninjaheroesnewera.com/)'s Ninja Income Automation Script<br/>
Script to suatomate Ninja Income claim for those who have many accounts.

## Preparation:
* Install [Python](https://www.python.org/downloads/) 3.8+
* Place your accounts detail inside `data.json`
* Install the packages needed by typing `pip install -r requirements.txt` on terminal
* (nh_claim.py: Optional) you can set the value of `BROWSER` variable inside `nh_claim.py` with either `chrome`, `edge` or `firefox` to make it easier later to run the script with just `nh_claim.py` or just run the script directly
<br />

## `nh_claim.py` (Discontinued)
~~Currently~~ Will only be supporting `Chrome`, `Edge`, and `Firefox` and only on `Windows` presumably <br/>
The script will run on your browser's private/incognito mode, except for `Firefox`.

To run:
1. Open `Windows Explorer` or just skip to step `5`
2. Get into the directory of `nh_claim.py` <br /> <img src="images\desktop-1.png"/>
3. Press `f4` button
4. Type `cmd` <br /> <img src="images\desktop-2.png"/>
5. Run the script by typing `nh_claim.py` followed by any browser listed above as an argument e.g. `nh_claim.py edge` then `enter`
6. If the driver is not there yet, it will download the proper driver executable of the selected browser and store it inside `driver\`. Just wait until it's done downloading <br /> <img src="images\desktop-3.png" title="nh_claim.py edge" alt="nh_claim.py edge" />
7. When the browser window showed, go get your coffee
<br />

## `nh_claim-fast.py`
It's the same with `nh_claim.py` but this uses `POST`/`GET` requests and also utilizing `multithreading` to claim the `Ninja Income`, and ~~significantly~~ ultimately more efficient than `nh_claim.py`.

To run:
1. Basically the same as `nh_claim.py`'s `1 - 4` instruction above
2. Run the script by typing `nh_claim-fast.py` followed by starting point e.g. `nh_claim-fast.py 1` then `enter` <br /> <img src="images\desktop-4.png" title="nh_claim-fast.py 1" alt="nh_claim-fast.py 1" />
3. Go get your coffee
<br />

## Mobile Users (`nh_claim-fast.py` only)
This tutorial is only intended and should be applicable for any smartphone that have access to Python environment.<br />
Originally I want to use [Termux](https://github.com/termux/termux-app) for universal tutorial on this, but I only have Android 5 smartphone in hand as of the time of writing this tutorial which isn't supported by the app

For first timers install these:
* Any JSON editor such as [JSON Editor](https://play.google.com/store/apps/details?id=com.nextmake.jsoneditor)
* Any Python IDE such as [Pydroid](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=en&gl=US) or run Python on any environment you want

To run:
1. Find, fill in the details and save on `data.json` using `JSON Editor`
2. Clone or download and unpack this repo to your mobile phone in any directory
3. Open `Pydroid`, reveal the side-menu <span><img src="images\mobile-1.png" height="20px"/></span> and press on `Terminal` <span><img src="images\mobile-2.png" height="20px"/></span>
4. Head to the repo directory using `cd` command e.g. `cd Download/NH_Income_Automation`
5. For first-time runners run `pip install -r requirements.txt`, and wait until it's done <br /> <img src="images\mobile-3.png" title="pip install -r requirements.txt" alt="pip install -r requirements.txt" />
6. Run the script using `python nh_claim-fast.py` or followed by starting point e.g. `python nh_claim-fast.py 1` <br /> <img src="images\mobile-4.png" title="python nh_claim-fast.py" alt="python nh_claim-fast.py" />

## Tips:
* When running `Python` script, you can put optional arguments in front of the command with `py` or whatever python executable set-up in the path e.g. `py nh_claim.py`
