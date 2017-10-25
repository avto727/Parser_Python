import requests
from requests.auth import HTTPBasicAuth

public_id = '***'
api_secret = '***'

# Для Refund
amount = '199'
transaction_id = '***'
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