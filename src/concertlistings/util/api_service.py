import requests

from concertlistings.models import Concert


class ApiService:

    token = '8Oil8TuZPSkCfN2bs0Vk8L3cbKb5dUgr'
    root_url = 'https://app.ticketmaster.com/discovery/v2'
    classification_id_music = 'KZFzniwnSyZfZ7v7nJ'
    events_endpoint = 'events'

    def get_concerts(self, state_code: str = 'NY', page: int = 0, size: int = 20) -> list[Concert]:
        concerts = []
        request_url = self.root_url + '/' + self.events_endpoint + '.json?apikey=' + self.token + \
                      '&classificationId=' + self.classification_id_music + '&stateCode=' + state_code \
                      + '&page=' + str(page) + '&size=' + str(size)
        response = requests.get(request_url)
        for event in response.json()['_embedded']['events']:
            concerts.append(self.create_concert(event))
        return concerts

    def get_concert_by_id(self, id: str) -> Concert:
        request_url = self.root_url + '/' + self.events_endpoint + '/' + id + '.json?apikey=' + self.token
        response = requests.get(request_url)
        return self.create_concert(response.json())

    @staticmethod
    def create_concert(event: dict) -> Concert:
        if event['id'] is None:
            return None

        id = event['id']
        title = event['name']
        try:
            artist = event['_embedded']['attractions'][0]['name']
        except KeyError:
            artist = ''
        try:
            venue = event['_embedded']['venues'][0]['name']
        except KeyError:
            venue = ''
        try:
            date = event['dates']['start']['dateTime']
        except KeyError:
            date = None
        try:
            genre = event['classifications'][0]['genre']['name']
        except KeyError:
            genre = ''
        try:
            price = (event['priceRanges'][0]['min'] + event['priceRanges'][0]['max']) / 2
        except KeyError:
            price = None
        ticket_url = event['url']
        try:
            image = event['images'][0]['url']
        except KeyError:
            image = None

        return Concert(
            id=id,
            title=title,
            artist=artist,
            venue=venue,
            date=date,
            genre=genre,
            price=price,
            ticket_url=ticket_url,
            image=image
        )
