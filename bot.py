"""
Calls the BC Developer Exchange API and tweets any issues added since the last time this process ran.
"""

import configparser
import logging.config
import os
import sys
import yaml
from helpers import StoredIssues, Tweet, BCDevExchangeIssues


class BCDeveloperExchangeBot:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger()

    def process(self):
        try:
            self.logger.info("Starting BC developer exchange bot")
            tweet = Tweet(self.config['twitter']['consumer_key'], self.config['twitter']['consumer_secret'],
                          self.config['twitter']['access_token'], self.config['twitter']['access_token_secret'])
            stored_issues = StoredIssues(self.config['file']['pickle_file'])
            seen_issues = stored_issues.get_seen_issues()
            issue_ids = []
            open_issues = BCDevExchangeIssues()
            for data in open_issues:
                issue_id, url, title = data
                if not (issue_id in seen_issues):
                    tweet.tweet_new_issue(url, title)
                else:
                    self.logger.info("Skipping {0}. Processed previously.".format(issue_id))
                issue_ids.append(issue_id)
            stored_issues.save_issues(issue_ids)
            self.logger.info("Completed BC developer exchange bot run.")
        except Exception as inst:
            self.logger.error(inst)
            raise

    def setup_logging(self):
        path = self.config['file']['logging_config']
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.load(f.read())
            logging.config.dictConfig(config)
        else:
            raise ValueError('Could not find ', path)

    def main(self):
        self.setup_logging()
        self.process()


if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
        bot_config = configparser.ConfigParser()
        bot_config.read_file(open(input_file))
        bot = BCDeveloperExchangeBot(bot_config)
        bot.main()
    except IndexError:
        print("Usage bot.py configFile.ini")
        sys.exit(1)
