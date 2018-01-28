# Auto Selling Bot For Coinbase Gdax
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
	docker build -t coinbase-autosell .; docker run -it -d \
	    -e  COINBASE_KEY \
	    -e  COINBASE_SECRET \
	    -e  GDAX_KEY \
	    -e  GDAX_SECRET \
	    -e  GDAX_PASSPHRASE \
	    --name cb-autosell  coinbase-autosell 