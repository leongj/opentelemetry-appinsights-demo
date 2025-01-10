# OpenTelemetry Observability Demo

This repository demonstrates how to use OpenTelemetry to collect and export telemetry data to [Azure Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) (part of Azure Monitor). It includes two methods for exporting telemetry data:
- **directly** from the application using the [Azure Monitor OpenTelemetry SDK](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python)
- **collector** - via a local [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) with the [Azure Monitor Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/azuremonitorexporter) configured, running in a Docker container.
  - *NOTE*: this method is [not officially supported by Microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-help-support-feedback?tabs=python#can-i-use-the-opentelemetry-collector)

## Prerequisites

- Azure Subscription ([create a free account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account))
  - Application Insights resource ([instructions](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource?tabs=bicep))
- Local
  - Python 3.10+
  - Docker Engine

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Make a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # In Powershell use `.venv\Scripts\Activate.ps1`
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```    

## Running the Direct Exporter Demo

1. Configure the environment based on the example file:
    ```sh
    cd direct
    cp .env.example .env
    ```

2. Edit `.env`:
    - You can get your `APPLICATION_INSIGHTS_CONNECTION_STRING` [from the Azure Portal](https://learn.microsoft.com/en-us/azure/azure-monitor/app/connection-strings).
    - Put in whatever `API_ENDPOINT` you want the app to call.

3. Run the client: `python client_direct.py`

## Running the Collector-based Demo

1. Configure the environment based on the example file:
    ```sh
    cd collector
    cp .env.example .env
    ```

2. Edit `.env` with whatever `API_ENDPOINT` you want the app to call.

3. Edit `otel-config.yaml` and update connection_string with your App Insights Connection String [from the Azure Portal](https://learn.microsoft.com/en-us/azure/azure-monitor/app/connection-strings).

4. Start the OpenTelemetry Collector using Docker Compose:
    ```sh
    docker-compose up
    ```

5. In a new terminal, run the [client_collector.py](http://_vscodecontentref_/11) script:
    ```sh
    source .venv/bin/activate  # In Powershell use `.venv\Scripts\Activate.ps1`
    cd collector
    python client_collector.py
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.