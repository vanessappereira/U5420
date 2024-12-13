"""
Investigate the datetime module and create a program that, when called without arguments, indicates the current date/time. 
Alternatively, it can receive one or two dates, indicating the number of days between these dates. 
If it only receives one date, it uses the current date as the second date. 
"""

import sys
from datetime import datetime, date


def alternateDays():
    if len(sys.argv) not in (1, 2, 3):
        print(f"Usage:{sys.argv[0]}  [date1] [date2]", file=sys.stderr)
        print("Date1/2 = YYYY-MM-DD", file=sys.stderr)
        sys.exit(2)
    if len(sys.argv) == 1:
        date1 = datetime.now()
        print(f"Actual date/hour: {date1}")
    else:
        dt1 = date.fromisoformat(sys.argv[1])
        dt2 = date.today() if len(sys.argv) == 2 else date.fromisoformat(sys.argv[2])
        print(f"Days between {dt1} and {dt2}: {(dt2-dt1).days()}")

def main():
    alternateDays()


if __name__ == "__main__":
    main()
