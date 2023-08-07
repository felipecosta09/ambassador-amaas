import json
import amaas.grpc
import time

# Set the variables
amaas_server = "antimalware.us-1.cloudone.trendmicro.com:443"
apikey = ""
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
