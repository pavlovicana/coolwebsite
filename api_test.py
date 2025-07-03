from woocommerce import API

wcapi = API(
    url="http://mystore.local",
    consumer_key="ck_dd315ad108ccdadde259eb1039c15ee08cde1385",
    consumer_secret="cs_a61bd18a8c7e7d396767151322ee4113e824b536",
    version="wc/v3"
)
r = wcapi.get("products")

print(r.json())