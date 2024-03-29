import logging 
import os 
from datetime import datetime

 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # output eg: Log file name: 03_14_2024_09_30_45.log
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #Log file path: /home/user/logs/03_14_2024_09_30_45.log (If /home/user/ is the cwd- then /logs/ with the file .log is joined on to it)
os.makedirs(logs_path, exist_ok = True)  # Create the directory if it doesn't exist.output : No output if the directory already exists. If the directory is created, it will return None.

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) #Full log file path: /home/user/logs/03_14_2024_09_30_45.log

logging.basicConfig(
    filename=LOG_FILE_PATH,                                                     #Output: No visible output, as the logging system is configured silently. 
                                                                                #However, any log messages emitted after this configuration will be written to the specified log file.
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

