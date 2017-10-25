import requests
from requests.auth import HTTPBasicAuth

public_id = 'pk_608b65f76ddfc8963b498a6e9a907'
api_secret = '32fdea530a3991a02a5a4714ac7d93c2'

# Для Refund
amount = '199'
transaction_id = '27540986'
params_1 = {
            'Amount': amount,
            'TransactionId': transaction_id
        }
# Для list_payments
# params_2 = {'Date': format_date(date)}
            # params['Timezone'] = 'MSK'

URL = 'https://api.cloudpayments.ru/payments/refund'
auth = HTTPBasicAuth(public_id, api_secret)

response = requests.post(URL, json=params_1, auth=auth)
print(response.text)