"""
    expected:
    >>> avatar_github('gvanrossum')
    'https://avatars.githubusercontent.com/u/2894642?v=4'

"""
import requests


def avatar_github(username: str) -> str:
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    return response.json()['avatar_url']


if __name__ == '__main__':
    print(avatar_github('miguelangellus'))
