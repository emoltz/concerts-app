from api_service import ApiService


def main():

    api_service = ApiService()

    response = api_service.get_concerts()
    print('datatype: {}\nresponse: {}'.format(type(response), response))


if __name__=='__main__':
    main()
