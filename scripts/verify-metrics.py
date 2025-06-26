import json
import sys

def verify_metrics(file_path, expected_metrics):
    with open(file_path, 'r') as f:
        data = json.load(f)

    # This is a very basic verification.
    # In a real scenario, you would have a more sophisticated way to check the metrics.
    if len(data['resourceMetrics']) > 0:
        print("Metrics found in the output file.")
        sys.exit(0)
    else:
        print("No metrics found in the output file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "test-output/metrics.json"
    
    verify_metrics(file_path, {})
