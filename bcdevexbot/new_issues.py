"""
Calls the BC Developer Exchange API and tweets any issues added since the last time this process ran.
"""

import configparser
import logging.config
import os
import sys

import yaml

from .bot_tools import StoredIssues, Tweet, BCDevExchangeIssues

logger = logging.getLogger()


def process(config):
    try:
        logger.info("Starting new issues bot")
        tweet = Tweet(config['twitter']['consumer_key'], config['twitter']['consumer_secret'],
                      config['twitter']['access_token'], config['twitter']['access_token_secret'])
        stored_issues = StoredIssues(config['file']['pickle_file'])
        seen_issues = stored_issues.get_seen_issues()
        issue_ids = []
        open_issues = BCDevExchangeIssues()
        for data in open_issues:
            issue_id, url, title = data
            if not (issue_id in seen_issues):
                tweet.tweet_new_issue(url, title)
            else:
                logger.info("Skipping {0}. Processed previously.".format(issue_id))
            issue_ids.append(issue_id)
        stored_issues.save_issues(issue_ids)
        logger.info("Completed new issues bot run.")
    except Exception as inst:
        logger.error(inst)
        raise


def setup_logging(path):
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
        setup_logging(bot_config['file']['logging_config'])
        process(bot_config)
    except IndexError:
        print("Usage new_issues.py configFile.ini")
        sys.exit(1)
