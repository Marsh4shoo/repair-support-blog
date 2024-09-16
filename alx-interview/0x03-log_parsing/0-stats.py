#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the current statistics"""
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

def signal_handler(sig, frame):
    """Handle the keyboard interruption signal (CTRL + C)"""
    print_stats()
    sys.exit(0)

# Set the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read and process each line from stdin
try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 7:
            try:
                # Extract status code and file size
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update total file size
                total_size += file_size

                # Update status code counts
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                # Ignore lines with invalid integers for status code or file size
                continue
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()
except Exception as e:
    pass

# Print final statistics after the loop ends
print_stats()
#!/usr/bin/python3

