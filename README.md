# Auto Selling Bot For Coinbase/Gdax
Automates converting BTC to EUR on Coinbase, via Gdax to avoid Coinbase's high fees.


### Auth
Api access to bot Coinbase and Gdax is required. The script expects these env variables:

- COINBASE_KEY
- COINBASE_SECRET	
- GDAX_KEY
- GDAX_SECRET
- GDAX_PASSPHRASE


### Run
	python3 autosell.py  
	
### Docker
Make vars.env with the required variables

	docker run -d -it --env-file vars.env --name cb-autosell  coinbase-autosell
