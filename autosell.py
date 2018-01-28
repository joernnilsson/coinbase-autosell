import gdax as GdaxClient
import pprint, time, os, sys, math
import logging
from coinbase.wallet.client import Client

spin_wait = 60*10

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        #logging.FileHandler("data/nicehash-autowithdraw.log"),
        logging.StreamHandler(sys.stdout)
    ])

logger = logging.getLogger(__name__)

BTC = "BTC"
EUR = "EUR"
BTC_EUR = "BTC-EUR"
pp = pprint.PrettyPrinter(indent=2)

def spin():

    # Setup clients
    cb = Client(os.environ["COINBASE_KEY"], os.environ["COINBASE_SECRET"])
    gdax = GdaxClient.AuthenticatedClient(os.environ["GDAX_KEY"], os.environ["GDAX_SECRET"], os.environ["GDAX_PASSPHRASE"])


    ### Transfer BTC from coinbase to gdax

    # Check for BTC balance on coinbase
    cb_accounts = cb.get_accounts()
    cb_account_btc = next(x for x in cb_accounts.data if x.currency == BTC)
    cb_btc_balance = float(cb_account_btc.balance.amount)
    logger.info("Coinbase BTC balance: %f", cb_btc_balance)

    # Deposit to gdax
    if(cb_btc_balance > 0.00001):
        logger.info("Transferring %f BTC from Coinbase to Gdax", cb_btc_balance)
        out = gdax.coinbase_deposit(amount=cb_btc_balance, currency=BTC, coinbase_account_id=cb_account_btc.id)
        # {'currency': 'BTC', 'id': 'c210d7.......b3023b77', 'amount': '0.00205565'}
        #if("id" in out):
        #    logger.info("Successfully transferred %f BTC from Coinbase to Gdax", cb_btc_balance)
        #print(out)
    
    ### Sell any BTC on gdax

    # Get BTC balance on gdax
    gdax_accounts = gdax.get_accounts()
    gdax_btc_account = next(x for x in gdax_accounts if x['currency'] == BTC)
    gdax_btc_balance = float(gdax_btc_account['balance'])
    logger.info("Gdax BTC balance: %f", gdax_btc_balance)
    #pp.pprint(gdax_btc_account)


    # Sell any BTC
    if(gdax_btc_balance > 0.00001):
        gdax.sell(size=str(gdax_btc_balance), product_id=BTC_EUR, type="market")


    ### Transfer EUR from gdax to coinbase
    gdax_eur_account = next(x for x in gdax_accounts if x['currency'] == EUR)
    gdax_eur_balance = float(gdax_eur_account['balance'])
    logger.info("Gdax EUR balance: %f", gdax_eur_balance)

    # Withdraw EUR 
    if(gdax_eur_balance > 0.01):
        cb_account_eur = next(x for x in cb_accounts.data if x.currency == EUR)
        #print(cb_account_eur)
        amt = '{0:.2f}'.format(math.floor(gdax_eur_balance*100)/100)
        logger.info("Transferring %s EUR from Gdax to Coinbase", amt)
        out = gdax.coinbase_withdraw(amount=amt, currency=EUR, coinbase_account_id=cb_account_eur.id)
        print(out)
        # error {'message': 'amount is required'}

if __name__ == "__main__":
    while(True):
        spin()
        #break
        time.sleep(spin_wait)



