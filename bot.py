"""
Calls the BC Developer Exchange API and tweets any issues added since the last time this process ran.
"""

import configparser
import logging.config
import os
import sys
import yaml
from helpers import StoredIssues, Tweet, BCDevExchangeIssues

logger = logging.getLogger(__name__)


def process(config):
    logger.info("Starting BC developer exchange bot")
    tweet = Tweet(config['twitter']['consumer_key'], config['twitter']['consumer_secret'],
                  config['twitter']['access_token'], config['twitter']['access_token_secret'])
    stored_issues = StoredIssues(config['file']['pickle_file'])
    seen_issues = stored_issues.get_seen_issues()
    issue_ids = []
    open_issues = BCDevExchangeIssues()
    # There are two try blocks because:
    # Inner try block deals with any exceptions while tweeting.  This allows for one issue to fail but allows for
    # the next issue to be processed.  Only the processed issue_ids will be stored.
    # The outer try block deals with the case where the response data could not be processed  (i.e. a field
    # is missing).  But, if any data had been successfully tweeted, then we want to store those issue ids.
    try:
        for data in open_issues:
            issue_id, url, title = data
            try:
                if not (issue_id in seen_issues):
                    tweet.tweet_new_issue(url, title)
                else:
                    logger.info("Skipping {0}. Processed previously.".format(issue_id))
            except Exception:
                logger.exception("Error while tweeting issue.")
            else:
                issue_ids.append(issue_id)
    except Exception:
        logger.exception("Error processing response.  May not have processed all the issues.")
        raise
    finally:
        stored_issues.save_issues(issue_ids)
        logger.info("Completed BC developer exchange bot run.")


def setup_logging(config):
    path = config['file']['logging_config']
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        raise ValueError('Could not find ', path)


if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
        bot_config = configparser.ConfigParser()
        bot_config.read_file(open(input_file))
        setup_logging(bot_config)
        process(bot_config)
    except IndexError:
        print("Usage bot.py configFile.ini")
        sys.exit(1)
    except Exception:
        logger.exception("Exception from bot run.")
        sys.exit(1)
