
from pathlib import Path
import json
from datetime import datetime
from loguru import logger

class SystemConfig:

    def __init__(self, path):
        self.path = Path(path)

        self.version = "0.0.1"
        self.last_updated = None

    def serialize(self):
        return {
            "version": self.version,
            "last_updated": str(datetime.now())
        }
    
    def deserialize(self, data):
        
        try:
            self.version = data['version']
            self.last_updated = data['last_updated']
        
        except Exception as error:
            print(error)

    def load(self):
        """ open the data file for the config """
        
        logger.debug("Loaded system config")
        with open( str(self.path), "r" ) as fp:
            data = json.load(fp)

    def dump(self):
        """ save a new instance of the config """
        
        logger.debug("Saved system config")
        with open( str(self.path), "w" ) as fp:
            json.dump(self.serialize(), fp, indent=3)