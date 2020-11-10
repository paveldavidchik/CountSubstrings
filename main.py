
import requests
import re


def main(url: str, substring: str):
    http_string = get_http_text(url)
    count = get_count_substrings(substring, http_string)
    print(count)


def get_http_text(url: str) -> str:
    if not url.startswith('https://'):
        url = 'https://' + url
    return requests.get(url).text


def get_count_substrings(substring: str, http_string: str) -> int:
    return len(re.findall(substring, http_string))


if __name__ == '__main__':
    main('tut.by', 'head')

