from .swap_api_consumer import SwapApiConsumer

def test_get_startships():
    '''Testing get_startships method'''

    swap_api_consumer = SwapApiConsumer()
    response = swap_api_consumer.get_startships(page = 1)

    print(response)