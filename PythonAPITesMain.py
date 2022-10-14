
from json.decoder import JSONDecodeError
import pytest
import requests




def main():
    payload={'name': 'User'}
    r = requests.Session()
    response = r.get('https://playground.learnqa.ru/api/hello')
    print(response.text)
    try:
        parsed_text=response.json()
    except JSONDecodeError:
        print('JSONDecodeError')


if __name__ == '__main__':
   main()
