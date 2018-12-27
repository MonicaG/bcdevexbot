"""Calls the Twitter help/configuration API and stores the results. Should only be run once a day!"""
import argparse
import configparser
import logging.config
import sys

from bcdevexbot import models


logger = logging.getLogger(__name__)


class TwitterConfig(models.Base):

    def process(self):
        logger.info("Starting Twitter Configuration process")
        tweet = self.get_twitter()
        tweet.reset_twitter_config()
        logger.info("Done Twitter Configuration process")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description=('Calls the twitter help/configuration API. '
                                                      'Should only be run once per day as per twitter documentation')
                                         )
    arg_parser.add_argument('config_file', help='Contains the configuration needed to run this process.')
    args = arg_parser.parse_args()
    twit_config = configparser.ConfigParser()
    twit_config.read_file(open(args.config_file))
    try:
        twitterConfig = TwitterConfig(twit_config)
        twitterConfig.setup_logging()
        twitterConfig.process()
    except Exception:
        logger.exception("twitter_configuration encountered an exception during its run.")
        sys.exit(1)
