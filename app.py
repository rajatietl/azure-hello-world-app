from flask import Flask
import os
from opencensus.ext.azure.log_exporter import AzureLogHandler

app = Flask(__name__)

# Application Insights configuration
app.logger.addHandler(AzureLogHandler(connection_string=os.getenv("APPINSIGHTS_CONNECTION_STRING")))

@app.route('/')
def hello_world():
    app.logger.info("Hello World endpoint was accessed")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
