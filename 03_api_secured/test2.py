# from facebook_business.api import FacebookAdsApi
# from facebook_business.adobjects.adaccount import AdAccount

# my_app_id = '1696381387180237'
# my_app_secret = '2e8c4e640bd999f94838ab90d904fa79'
# my_access_token = 'EAAYG2ZAH8iM0BAEszmfOaZAQ5qr6FW2JyUe2biPyCq02PUHsZAYrOGS1TFH4W1CV8ZBxqY2ENLSqL0tMWsffSU0FNPU7BJZCVG4A50BNyebI0bulWk3oX3GCDL4ZBKnw38qdt7cjXbqq2ZAg7tMuv3fIzCl7Fqnw6nB2uYemLRoHRzuwEgXycVW9422PMGhX99wVCZBpqA0dsz8x2dsCC58K'
# FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
# my_account = AdAccount('act_642303109628222')
# campaigns = my_account.get_campaigns()
# print(campaigns)


from facebookads.objects import AdAccount, Ad

account_id = 'act_1696381387180237'
ad_account = AdAccount(account_id)
ad_iter = ad_account.get_ads(fields=[Ad.Field.name])
for ad in ad_iter:
    print(ad[Ad.Field.name])