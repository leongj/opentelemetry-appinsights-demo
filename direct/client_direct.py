# This program uses the direct exporter method to send telemetry data to Azure Monitor.
# https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python

import os
import requests
import time
from dotenv import load_dotenv

from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace

load_dotenv()

# Configure OpenTelemetry - picks up config from .env
configure_azure_monitor()

# This file uses automatic instrumentation. To define manual tracing, refer to: 
# https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/monitor/azure-monitor-opentelemetry/samples/README.md

# call the API in infinite loop with sleep
while True:
    uri = os.getenv("API_ENDPOINT")
    print("Calling API:", uri)

    response = requests.get(uri)
    
    print(f"Status: {response.status_code}")
    print(f"{response.text}")
    time.sleep(2)
