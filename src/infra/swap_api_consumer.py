import requests

class SwapApiConsumer:

    @classmethod
    def get_startships(self, page: int): 
        param = {'page': page}
        response = requests.get('https://swapi.dev/api/starships/', params= param)

        return response.json()

