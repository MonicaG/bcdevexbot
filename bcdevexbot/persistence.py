import logging
import pickle

logger = logging.getLogger(__name__)


class DataStore:
    """Store and retrieve data using a pickle file"""
    def __init__(self, pickle_file_path):
        self._pickle_file_path = pickle_file_path

    def save(self, data):
        with open(self._pickle_file_path, 'wb') as f:
            pickle.dump(data, f)

    def get(self):
        try:
            with open(self._pickle_file_path, 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            logger.exception("Could not find the file " +
                             self._pickle_file_path)
            raise
        else:
            return data
