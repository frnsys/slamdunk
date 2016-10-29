import json
import config
import requests
from time import sleep
from arena import Arena


def slack(msg):
    requests.post(config.SLACK_WEBHOOK_URL,
                  data=json.dumps({'text': msg}))


if __name__ == '__main__':
    seen = set()
    api = Arena(config.ARENA_TOKEN)

    while True:
        feed = [i['item'] for i in api.feed()['items']]
        for item in feed:
            id = item['id']
            if id in seen:
                continue
            seen.add(id)
            type = item['class']
            if type == 'Image':
                slack('Image, added by {user}\n{image}'.format(
                    user=item['user']['full_name'],
                    image=item['image']['display']['url']
                ))
            elif type == 'Channel':
                # for now, skipping channels
                continue
            elif type == 'Link':
                slack('*{title}* (<{url}>, added by {user})\n{description}\n{image}'.format(
                    title=item['title'],
                    url=item['source']['url'],
                    description=item['description'],
                    user=item['user']['full_name'],
                    image=item['image']['display']['url']
                ))

        sleep(config.WAIT_TIME)