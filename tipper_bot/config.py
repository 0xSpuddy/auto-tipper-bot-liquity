import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# update these values
network = os.getenv("NETWORK") # ganache, goerli, mainnet, mumbai, polygon
query_id = os.getenv("QUERY_ID")
query_data = os.getenv("QUERY_DATA")
interval = int(os.getenv("INTERVAL")) # in seconds
chainlink_is_frozen_timeout = int(os.getenv("CHAINLINK_IS_FROZEN_TIMEOUT"))
chainlink_max_price_deviation = float(os.getenv("CHAINLINK_MAX_PRICE_DEVIATION_FROM_PREVIOUS_ROUND"))

if network == "mainnet":
    provider_url = os.getenv("PROVIDER_URL_MAINNET")
    oracle_address = "0xD9157453E2668B2fc45b7A803D3FEF3642430cC0"
    oracle_token_address = "0x88dF592F8eb5D7Bd38bFeF7dEb0fBc02cf3778a0"
    autopay_address = "0x9BE9B0CFA89Ea800556C6efbA67b455D336db1D0"
    private_key = os.getenv("MAINNET_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    base_token_price_url_selector = "ethereum"
    gas_price_url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
elif network == "goerli":
    provider_url = os.getenv("PROVIDER_URL_GOERLI")
    oracle_address = "0xD9157453E2668B2fc45b7A803D3FEF3642430cC0"
    oracle_token_address = "0x51c59c6cAd28ce3693977F2feB4CfAebec30d8a2"
    autopay_address = "0x9BE9B0CFA89Ea800556C6efbA67b455D336db1D0"
    private_key = os.getenv("GOERLI_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    base_token_price_url_selector = "ethereum"
    gas_price_url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
elif network == "goerli_playground":
    provider_url = os.getenv("PROVIDER_URL_GOERLI")
    oracle_address = "0x3251838bd813fdf6a97D32781e011cce8D225d59"
    oracle_token_address = "0x3251838bd813fdf6a97D32781e011cce8D225d59"
    autopay_address = "0x9F6091CD579304a27Cf8Ab4927b1e0c242F61B4D"
    private_key = os.getenv("GOERLI_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    base_token_price_url_selector = "ethereum"
    gas_price_url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
elif network == "polygon":
    provider_url = os.getenv("PROVIDER_URL_POLYGON")
    oracle_address = "0xD9157453E2668B2fc45b7A803D3FEF3642430cC0"
    oracle_token_address = "0xE3322702BEdaaEd36CdDAb233360B939775ae5f1"
    autopay_address = "0x9BE9B0CFA89Ea800556C6efbA67b455D336db1D0"
    private_key = os.getenv("POLYGON_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=usd"
    base_token_price_url_selector = "matic-network"
    gas_price_url = "https://api.polygonscan.com/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
elif network == "mumbai":
    provider_url = os.getenv("PROVIDER_URL_MUMBAI")
    oracle_address = "0xD9157453E2668B2fc45b7A803D3FEF3642430cC0"
    oracle_token_address = "0xCE4e32fE9D894f8185271Aa990D2dB425DF3E6bE"
    autopay_address = "0x9BE9B0CFA89Ea800556C6efbA67b455D336db1D0"
    private_key = os.getenv("MUMBAI_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=usd"
    base_token_price_url_selector = "matic-network"
    gas_price_url = "https://api.polygonscan.com/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
elif network == "optimism":
    provider_url = os.getenv("PROVIDER_URL_OPTIMISM")
    oracle_address = "0xD9157453E2668B2fc45b7A803D3FEF3642430cC0"
    oracle_token_address = "0xaf8cA653Fa2772d58f4368B0a71980e9E3cEB888"
    autopay_address = "0x9BE9B0CFA89Ea800556C6efbA67b455D336db1D0"
    private_key = os.getenv("OPTIMISM_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    base_token_price_url_selector = "ethereum"
    gas_price_url = "https://api-optimistic.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=YourApiKeyToken" # not used
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
elif network == "optimism-goerli":
    provider_url = os.getenv("PROVIDER_URL_OPTIMISM_GOERLI")
    oracle_address = "0xD9157453E2668B2fc45b7A803D3FEF3642430cC0"
    oracle_token_address = "0xd71F72C18767083e4e3FE84F9c62b8038C1Ef4f6"
    autopay_address = "0x9BE9B0CFA89Ea800556C6efbA67b455D336db1D0"
    private_key = os.getenv("OPTIMISM_GOERLI_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    base_token_price_url_selector = "ethereum"
    gas_price_url = "https://api-optimistic.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=YourApiKeyToken" # not used
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
elif network == "ganache":
    provider_url = os.getenv("PROVIDER_URL_GANACHE")
    oracle_address = "0x9985C500268a2dA5dfc9f643125F9f2FD2DEaD68"
    oracle_token_address = "0x9985C500268a2dA5dfc9f643125F9f2FD2DEaD68"
    autopay_address = "0x0addEeE0a4a5E17bee897CbBE0B57a950d383aBF"
    private_key = os.getenv("GANACHE_PK")
    oracle_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=tellor&vs_currencies=usd"
    oracle_token_price_url_selector = "tellor"
    base_token_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    base_token_price_url_selector = "ethereum"
    gas_price_url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
    chainlink_aggregator_address = os.getenv("CHAINLINK_AGGREGATOR_ADDRESS")
else:
    print("invalid network")


# can change these values or leave them as is
start_time = datetime.datetime(2022, 12, 1, 0, 0, 0) # start time for the first interval
initial_profit_margin_usd = 2.0 # usd
tip_multiplier = 1.10 # multiplier for each tip retry
max_retip_count = 10 # max number of times to retry a tip
retip_delay = 45 # seconds
total_gas_cost=700000 # cost of submitValue + claimTip
api_max_tries = 10 # max number of times to retry api calls
token_approval_amount = 1000e18 # amount of oracle token to approve for autopay contract



