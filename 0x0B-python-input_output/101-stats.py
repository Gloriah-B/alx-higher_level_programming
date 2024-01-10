#!/usr/bin/python3
import sys

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

try:
    count = 0
    for line in sys.stdin:
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            metrics['total_file_size'] += file_size
            metrics['status_codes'][status_code] += 1

            count += 1

            if count % 10 == 0:
                print(f"File size: {metrics['total_file_size']}")
                for code, value in sorted(metrics['status_codes'].items()):
                    if value != 0:
                        print(f"{code}: {value}")

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    print(f"File size: {metrics['total_file_size']}")
    for code, value in sorted(metrics['status_codes'].items()):
        if value != 0:
            print(f"{code}: {value}")
