
from loguru import logger
from pathlib import Path
import shutil
from basicapp.models.system_config import SystemConfig
import sys



class FileManager:
    storage_path = Path(Path.home()) / "basicapp"
    
    def __init__(self):

        # initialize logger first so that other modules get the correct configuration
        self.logger_path = self.storage_path / "logs"

        try:
            config = {
                "handlers": [
                    {"sink": sys.stdout, "format": "{time} - {message}", "level": "ERROR"},
                    {"sink": str(self.logger_path / "log.txt")},
                ]
            }
            logger.configure(**config)
        except Exception as err:
            print(f">>> {err}")

        # setup system config path
        logger.info("setup logger successfully")
        self.system_config_path = self.storage_path / "config.json"
        
    def install(self):
        
        # create directory
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # create config
        sys_conf = SystemConfig( path=str(self.system_config_path) )
        sys_conf.dump()
        

    def uninstall(self): 

        # delete system storage location and all related files
        shutil.rmtree(str(self.storage_path))


