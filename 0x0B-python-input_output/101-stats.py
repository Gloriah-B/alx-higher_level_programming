import sys


def process_logs():
    metrics = {
        'total_file_size': 0,
        'status_codes': {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
        }
    }

    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                if len(parts) < 3:
                    # Log line doesn't match expected format, skipping
                    continue

                status_code = int(parts[-2])
                file_size = int(parts[-1])

                metrics['total_file_size'] += file_size
                metrics['status_codes'][status_code] += 1

                count += 1

                if count % 10 == 0:
                    print_metrics(metrics)

            except (ValueError, IndexError):
                # Log line parsing error, skipping
                continue

    except KeyboardInterrupt:
        print_metrics(metrics)


def print_metrics(metrics):
    print(f"File size: {metrics['total_file_size']}")
    for code, value in sorted(metrics['status_codes'].items()):
        if value != 0:
            print(f"{code}: {value}")


if __name__ == "__main__":
    process_logs()
