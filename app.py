from flask import Flask
import os
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

app = Flask(__name__)

# Configure logging with timestamp
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=os.getenv("APPINSIGHTS_CONNECTION_STRING")))

@app.route('/')
def hello_world():
    logger.info("Hello World endpoint was accessed")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
