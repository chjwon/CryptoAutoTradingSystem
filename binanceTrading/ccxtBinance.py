# WIP
import ccxt

apiKeyTXT = open('apiKey.txt','r')
apiKey = apiKeyTXT.read()
# apiKeyTXT.close()

secretTXT = open('secret.txt','r')
secret = secretTXT.read()
# secretTXT.close()

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': apiKey,
    'secret': secret,
})

