import os
import requests
import ast

from concertlistings.models import Concert

class ApiService:

    # token = os.environ.get('TM_API_KEY')
    token = '8Oil8TuZPSkCfN2bs0Vk8L3cbKb5dUgr'
    root_url = 'https://app.ticketmaster.com/discovery/v2'
    classification_name = 'Music'
    classification_id = 'KZFzniwnSyZfZ7v7nJ'
    events_endpoint = 'events'

    def get_concerts(self, state_code: str = 'NY', page_size: int = 5) -> list[Concert]:
        request_url = self.root_url + '/' + self.events_endpoint + '.json?apikey=' + self.token + \
                      '&classificationId=' + self.classification_id + '&stateCode=' + state_code + '&size' + \
                      str(page_size)
        response = requests.get(request_url)
        return self.format_response(response)

    @staticmethod
    def format_response(response) -> list[Concert]:
        formatted_response = []
        for event in response.json()['_embedded']['events']:
            formatted_response.append(Concert(
                id=event['id'],
                title=event['name'],
                artist=event['_embedded']['attractions'][0]['name'],
                venue=event['_embedded']['venues'][0]['name'],
                date=event['dates']['start']['dateTime'],
                genre=event['classifications'][0]['genre']['name'],
                price=(event['priceRanges'][0]['min']+event['priceRanges'][0]['max'])/2,
                ticket_url=event['url'],
            ))
        return formatted_response
