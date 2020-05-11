""" Calls the BC Developer Exchange API and tweets any issues added since the last time this process ran. """

import argparse
import configparser
import logging.config
import sys

from bcdevexbot import models, persistence

logger = logging.getLogger(__name__)


class BCDevExBot(models.Base):

    def process(self):
        logger.info("Starting BC developer exchange bot")
        tweet = self.get_twitter()
        stored_issues = persistence.DataStore(self.config['file']['pickle_file'])
        seen_issues = stored_issues.get()
        issue_ids = []
        open_issues = models.BCDevExchangeIssues().get_opportunities()
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
            logger.exception("Error processing response data.")
            raise
        finally:
            stored_issues.save(issue_ids)
            logger.info("Completed BC developer exchange bot run.")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description=('Calls the BC Developer Exchange API and tweets any issues '
                                                      'added since the last time this process ran.')
                                         )
    arg_parser.add_argument('config_file', help='Contains the configuration needed to run this bot')
    args = arg_parser.parse_args()
    bot_config = configparser.ConfigParser()
    bot_config.read_file(open(args.config_file))
    try:
        bot = BCDevExBot(bot_config)
        bot.setup_logging()
        bot.process()
    except Exception:
        logger.exception("Bot encountered an exception during its run.")
        sys.exit(1)
