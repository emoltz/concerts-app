import os
import requests

from concertlistings.models import Concert


class ApiService:

    token = '8Oil8TuZPSkCfN2bs0Vk8L3cbKb5dUgr'
    root_url = 'https://app.ticketmaster.com/discovery/v2'
    classification_name = 'Music'
    classification_id = 'KZFzniwnSyZfZ7v7nJ'
    events_endpoint = 'events'

    def get_concerts(self, state_code: str = 'NY', page_size: int = 5) -> list[Concert]:
        concerts = []
        request_url = self.root_url + '/' + self.events_endpoint + '.json?apikey=' + self.token + \
                      '&classificationId=' + self.classification_id + '&stateCode=' + state_code + '&size' + \
                      str(page_size)
        response = requests.get(request_url)
        for event in response.json()['_embedded']['events']:
            concerts.append(self.create_concert(event))
        return concerts

    def get_concert_by_id(self, id: str) -> Concert:
        request_url = self.root_url + '/' + self.events_endpoint + '/' + id + '.json?apikey=' + self.token
        response = requests.get(request_url)
        return self.create_concert(response)

    @staticmethod
    def create_concert(event: dict) -> Concert:
        return Concert(
            id=event['id'],
            title=event['name'],
            artist=event['_embedded']['attractions'][0]['name'],
            venue=event['_embedded']['venues'][0]['name'],
            date=event['dates']['start']['dateTime'],
            genre=event['classifications'][0]['genre']['name'],
            price=(event['priceRanges'][0]['min']+event['priceRanges'][0]['max'])/2,
            ticket_url=event['url'],
        )
