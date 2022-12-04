## Setup and run 
## For MacOS/LinuxOS
`source env.sh`

`python -m venv venv`

`source venv/bin/activate`

`python -m pip install --upgrade pip`

`$export ETH_RPC_URL=<your ETH_RPC_URL> before launching jupyter-lab` 

`$export ExRatesAPI_KEY=<your ExRates API KEY>`

`jupyter-lab or VScode with Jupyter Notebook extension` 

## For Bash on WindowsOS
`source env.sh`

`python -m venv venv`

`source venv/Scripts/activate` 

`python -m pip install --upgrade pip`

`add ETH_RPC_URL=<your ETH_RPC_URL> as a NEW user variable -> Windows Settings -> Advanced System Settings -> Advanced Tab -> Environment Variables -> User Variables for USER` 

`add ExRatesAPI_KEY=<your ExRates API KEY> as a NEW user variable -> Windows Settings -> Advanced System Settings -> Advanced Tab -> Environment Variables -> User Variables for USER`

`jupyter-lab or VScode with Jupyter Notebook extension`