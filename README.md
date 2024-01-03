# NH_Income_Automation
[Ninja Heroes: New Era](https://www.ninjaheroesnewera.com/)'s Ninja Income Automation Script <br />
Script to automate Ninja Income claim for those who have many accounts.

# Installation
1. Install [Python](https://www.python.org/downloads/) 3.8+
2. Download or clone the repository:
    ```bash
    git clone https://github.com/Insisted/NH_Income_Automation.git
    ```
3. Get into the directory of the project <br /> <img src="images\desktop-1.png" title="Project Path" alt="Project Path" />
4. Press `[Shift] Right Click` on the directory
5. Click on `Open in (Terminal|Command Prompt|PowerShell)`
6. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
7. Find and fill in the accounts details in `data.json`

# `nh_claim-fast`
Automation script using `POST`/`GET` requests, utilizing `multithreading` to claim the `Ninja Income`, and ~~significantly~~ ultimately more efficient than [`nh_claim.py`](#nh_claim-discontinued).

To run:
1. Basically the same as [Installation](#installation)'s `3 - 5` instruction above
2. Run the script by double clicking or executing `nh_claim-fast.py` on terminal, with or without the starting point e.g.
    ```bash
    nh_claim-fast.py 1
    ```
    <img src="images\desktop-2.png" width="649" title="nh_claim-fast.py 1" alt="nh_claim-fast.py 1" />
3. Just wait for it to finish

## Mobile Users (`nh_claim-fast` only)
This tutorial is only intended and should be applicable for any smartphone that have access to Python environment. <br />
In this tutorial I will use [Termux](https://termux.dev/)

### Mobile Installation
1. Install Termux from [Github](https://github.com/termux/termux-app/releases/) or [F-Droid](https://f-droid.org/en/packages/com.termux/) or run Python on any environment you want
2. Install Python3 from Termux:
    ```bash
    yes | pkg upgrade
    pkg install python3 -y
    ```
3. Download and unpack or clone the repository from Termux:
    ```bash
    pkg install git
    git clone https://github.com/Insisted/NH_Income_Automation.git
    ```
4. Get into the directory of the project
    * If downloaded:
        1. Execute
            ```bash
            termux-setup-storage
            ```
        2. use `cd` command to get into the extracted folder e.g.
            ```bash
            cd storage/downloads/NH_Income_Automation-main
            ```
    * If cloned: 
        1. use `cd` command to get into the cloned repo
            ```bash
            cd NH_Income_Automation
            ```
    <img src="images\mobile-2.png" width="649" title="cd <dir_path>" alt="cd <dir_path>" />
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Find and fill in the accounts details in `data.json`
    * If downloaded:
        1. Edit the JSON file using any text editor and save it
    * If cloned: 
        1. use `nano` command to edit the JSON file **(Copy from another text editor and paste it inside to make it easier)**
            ```bash
            nano data.json
            ```
        2. After you're done, press <img src="images\mobile-1.png" height="20px" title="CTRL Button" alt="CTRL Button"/> from the menu and `X` on your keyboard
        3. Press `Y` on your keyboard, then `Enter`

To run:
1. Basically the same as [Mobile Installation](#mobile-installation)'s `4` instruction above
2. Run the script by executing `nh_claim-fast.py` on terminal, with or without the starting point e.g.
    ```bash
    python nh_claim-fast.py 1
    ```
    <img src="images\mobile-3.png" width="649" title="python nh_claim-fast.py" alt="python nh_claim-fast.py" />

# `nh_claim` (Discontinued)
~~Currently~~ Will only be supporting `Chrome`, `Edge`, and `Firefox` and only on `Windows` presumably. <br />
The script will run on your browser's private/incognito mode, except for `Firefox`. <br />
you can set the value of `BROWSER` variable inside `nh_claim.py` with either `chrome`, `edge` or `firefox` to make it easier later to run the script with just `nh_claim.py` or just run the script directly

To run:
1. Basically the same as [Installation](#installation)'s `3 - 5` instruction above
2. Run the script by double clicking or executing `nh_claim.py` on terminal, followed by any browser listed above as an argument e.g. `nh_claim.py edge`
3. If the driver is not there yet, it will download the proper driver executable of the selected browser and store it inside `driver\`. Just wait until it's done downloading <br /> <img src="images\desktop-3.png" width="649" title="nh_claim.py edge" alt="nh_claim.py edge" />
4. When the browser window showed, go get your coffee


# Tips
* When running `Python` script, you can put optional arguments in front of the command with `py` or whatever python executable set-up in the path e.g. `py nh_claim.py`
