# import requests
#
# updated_post = {
#     'title': 'updated title',
#     'body': 'updated body',
#     'userId': 1
# }
# post_id = 1
# response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=updated_post)
# if response.status_code == 200:
#     post = response.json()
#     print(f"Post updated: ID: {post['id']}, Title: {post['title']}, Body: {post['body']}")
# else:
#     print(f'Failed to update post with ID {post_id}')


# konwersja PLN to -> KRW

import requests


api_key = 'aeffe81cec40f4f17bab8507'
base_url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/PLN/USD'

response = requests.get(base_url)
if response.status_code == 200:
    exchange_data = response.json()
    pln_to_usd = exchange_data.get('conversion_rate')

    price_pln = 250
    price_krw = price_pln * pln_to_usd

    print(f"Cena: {price_pln} PLN")
    print(f"Cena w USD: {price_krw:.2f} USD")
else:
    print('Nieudało się pobrać kursu wymiany walut')