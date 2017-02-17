import requests


def getit(cursor='1:0:0'):

    response = requests.get('https://disqus.com/api/3.0/threads/listPostsThreaded?limit=50&thread=5558487974&forum=breitbartproduction&order=popular&cursor=' + cursor + '&api_key=E8Uh5l5fHZ6gD8U3KycjAIAk46f68Zw7C6eW8WSjZvCLXebZ7p0r1yrYDrLilk2F').json()

    responses = response['response']

    for r in responses:
        print r['raw_message']

    nextcursor = response['cursor']['next']
    getit(nextcursor)

# pagination
# next_cursor in json

# copy xhr as curl in network tab
# convert curl command to python requests
