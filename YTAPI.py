import json
import requests


def search_with_api(query):
    search = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&q="+ query + "&type=video&key=*censored*")
    results = json.loads(search.text)
    print(type(results))
    for entry in results['items']:
        print(type(entry))
        video = entry['id']['videoId']
        break

    url = 'https://www.youtube.com/watch?v=' + str(video)
    return url

if __name__ == '__main__':
    query = (input('query: '))
    search_with_api(query)


