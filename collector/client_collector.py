from dotenv import load_dotenv
import os
import requests
import time

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Define OpenTelemetry Resource from environment variables
load_dotenv()
SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME")
SERVICE_INSTANCE_ID = os.getenv("OTEL_RESOURCE_ATTRIBUTES").split('service.instance.id=')[1]
resource = Resource.create({ "service.name": SERVICE_NAME, "service.instance.id": SERVICE_INSTANCE_ID })
print(f"\nSERVICE_NAME: {SERVICE_NAME}")
print(f"SERVICE_INSTANCE_ID: {SERVICE_INSTANCE_ID}\n")

# Setup Tracer, with export using OTLP to the collector at localhost
traceProvider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True))
traceProvider.add_span_processor(processor)
trace.set_tracer_provider(traceProvider)
tracer = trace.get_tracer("python-otel-tracer")

# Enable automatic instrumentation - requires Tracer to be configured above
RequestsInstrumentor().instrument()


print("Calling API in infinite loop, Ctrl+C to stop...\n")
uri = os.getenv("API_ENDPOINT")
while True:
    print("Calling API:", uri)
    response = requests.get(uri)
    
    print(f"Status: {response.status_code}")
    print(f"{response.text}\n")

    time.sleep(2)