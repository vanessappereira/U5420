"""Calculates time in seconds after entering hours, minutes, and
seconds.

INPUT DATA:
    hours   : h, string -> int
    minutes : m, string -> int
    seconds : s, string -> int

OUTPUT DATA:
    seconds : total_secs, int
    total_secs = h*3600 + m*60 + s """


def calculate_time():
    hour = int(input("Hours: "))
    minute = int(input("Minutes: "))
    second = int(input("Seconds: "))
    total_secs = hour * 3600 + minute * 60 + second

    print(f"Total: {total_secs} seconds")


if __name__ == "__main__":
    calculate_time()  # call the function with arguments
