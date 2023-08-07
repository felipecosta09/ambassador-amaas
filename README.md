# Workshop AMaaS

## Introduction
Cloud One VSAPI is a Software Development Kit (SDK) that allows you to integrate Trend Micro's malware scanning capabilities into your applications, by allowing you to scan files and determine whether they are malicious or not. The interaction with the AMaaS backend service is facilitated through an SDK that enables you to send files to the backend service. The backend service utilizes the Trend Micro Antimalware engine and the Trend Micro Smart Protection Network (SPN) for file scanning.

The SDK is available in the following programming languages:
- Python
- Node.js/typescript
- Go
- Java* (Coming soon)

## Prerequisites

- Have an [Trend Cloud One Account](https://cloudone.trendmicro.com). [Sign up for free trial now](https://cloudone.trendmicro.com/trial) if it's not already the case!
- A [Trend Cloud One API Key](https://cloudone.trendmicro.com/docs/identity-and-account-management/c1-api-key/#new-api-key)
- A [Trend Cloud One Region](https://cloudone.trendmicro.com/docs/identity-and-account-management/c1-regions/) of choice
- Python 3.7 or newer
- A file or object to be scan

## Installation

Install the VSAPI SDK package with pip:

```sh
python -m pip install cloudone-vsapi
```

## Usage

1 - Start a container with the following command:

```sh
docker run -it python:3.9 bash
```

2 - Update the package manager and install vim:
  
  ```sh
  apt-get update && apt-get install vim -y
  ```

3 - Install the VSAPI SDK package with pip:

```sh
python -m pip install cloudone-vsapi
```

4 - Download a eicar file:

```sh
wget https://secure.eicar.org/eicar.com
```

5 - Create a file named `scan.py` and copy the following code:

```python
import json
import amaas.grpc
import time

# Set the variables
amaas_server = "antimalware.us-1.cloudone.trendmicro.com:443"
apikey = "YOUR_API_KEY"
filename = "eicar.com"

# Initialize the gRPC client, True for TLS
handle = amaas.grpc.init(amaas_server,apikey,True)

# Scan the file and set a timer counter
s = time.perf_counter()
scan = amaas.grpc.scan_file(filename, handle)
elapsed = time.perf_counter() - s

# Print the result
result = json.loads(scan)
result['scanDuration'] = f"{elapsed:0.2f}s"
print(json.dumps(result, indent=4))

# Quit the gRPC client
amaas.grpc.quit(handle)

```
**PS.: Replace the apikey variable with your API Key.**

## Results

You should see the following output:

```json

{
    "version": "1.0.0",
    "scanResult": 1,
    "scanId": "9fe71b98-a8e0-4030-b711-8f88119fae8e",
    "scanTimestamp": "2023-08-04T19:46:28.707Z",
    "fileName": "eicar.com",
    "foundMalwares": [
        {
            "fileName": "eicar.com",
            "malwareName": "Eicar_test_file"
        }
    ]
}

```

## Conclusion
Congratulations! You have successfully integrated Trend Micro's malware scanning capabilities into your application. You can now scan files for malware.
