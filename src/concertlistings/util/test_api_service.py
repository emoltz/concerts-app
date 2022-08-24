from api_service import ApiService


def main():

    api_service = ApiService()

    response = api_service.get_concerts()
    concert = api_service.get_concert_by_id('G5vVZ9dLbWv5L')
    print('datatype: {}\nresponse: {}'.format(type(response), response))


if __name__=='__main__':
    main()
