# slamdunk

simple slackbot that brings your [are.na](https://www.are.na/) feed into a slack channel.

## setup

install the requirements:

    pip install -r requirements.txt

create `config.py` in the following format:

```python
# how long to wait between updates
WAIT_TIME = 60 * 10

# your are.na token (visit <https://dev.are.na>)
# (the "Personal Access Token")
ARENA_TOKEN = 'your are.na token'

# your slack webhook url;
# from in your slack group, click the name of the group,
# then select "Apps & integrations", click "Build",
# select "Make Custom Integration", select "Incoming Webhooks",
# set it all up there and put the webhook url here
SLACK_WEBHOOK_URL = 'your slack webhook url'
```

then just run `main.py`!