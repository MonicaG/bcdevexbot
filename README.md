# bcdevexbot
[![Build Status](https://travis-ci.org/MonicaG/bcdevexbot.svg?branch=master)](https://travis-ci.org/MonicaG/bcdevexbot)

This is the code base for the [@bcdevexbot](https://twitter.com/bcdevexbot) twitter bot.

The bot calls the [https://digital.gov.bc.ca/marketplace/api/opportunities/sprint-with-us/](https://digital.gov.bc.ca/marketplace/api/opportunities/sprint-with-us/)  and [https://digital.gov.bc.ca/marketplace/api/opportunities/code-with-us/](https://digital.gov.bc.ca/marketplace/api/opportunities/code-with-us/)APIs and tweets any opportunities that have been added since the last time the bot ran.

Two processes make up the bot:

1. [bot.py](bot.py) - The bot.  It reads the API and tweets any new issues
2. [twitter_configuration.py](twitter_configuration.py) - Gets the [twitter help configuration](https://dev.twitter.com/rest/reference/get/help/configuration) values and stores them.  Only runs once a day.

## Example config file
Example config file needed for the bot.py and twitter_configuration.py processes.

```
[twitter]
consumer_key = nnnn
consumer_secret = xxxx
access_token = yyyy
access_token_secret = zzzz

[file]
pickle_file = /path/to/file/issues.pickle
twitter_help_config = /path/to/file/twitter_help_config.pickle
logging_config = /path/to/file/config/logging.yaml
```

## Disclaimer
Not affiliated with the [https://digital.gov.bc.ca/marketplace/opportunities](https://digital.gov.bc.ca/marketplace/opportunities) site or the Province of British Columbia.
