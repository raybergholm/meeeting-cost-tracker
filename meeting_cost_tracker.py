#!/usr/bin/env python3

import argparse
import datetime
import time

DEFAULT_CURRENCY = "euros"
DEFAULT_WORKING_HOURS = "37.5"

'''
Mac doesn't like the keyboard module and I don't like having to sudo it all the time.
This version doesn't let you do on-the-fly participant count adjustments so meh
'''


def main():
    args = parse_cli_arguments()

    currency_symbol = args.currency_symbol
    working_hours_per_week = float(args.working_hours)

    start_time = time.time()
    start_datetime = datetime.datetime.now()
    end_time = None
    end_datetime = None
    time_elapsed = None
    cumulative_cost = 0.0

    print("Meeting started on {0} at {1}".format(
        start_datetime.strftime("%d.%m"), start_datetime.strftime("%I:%M:%S %p")))

    # Block until we're done
    exit = False
    while not exit:
        user_input = input("Is the meeting over? y/n ")
        if user_input.lower() == "y":
            exit = True

    end_time = time.time()
    end_datetime = datetime.datetime.now()
    print("Meeting finished on {0} at {1}".format(
        end_datetime.strftime("%d.%m"), end_datetime.strftime("%I:%M:%S %p")))

    participants = None
    while participants == None:
        try:
            user_input = int(input("How many people were in the meeting? "))

            if user_input <= 1:
                print("There's probably more people than that?")
            else:
                participants = user_input

        except ValueError:
            print("Integer please!")

    average_salary = None
    while average_salary == None:
        try:
            average_salary = float(
                input("How many people were in the meeting? "))

        except ValueError:
            print("Couldn't parse that!")

    time_elapsed = end_time - start_time
    cost_per_second = (average_salary/(4*working_hours_per_week))/3600
    cumulative_cost = participants * cost_per_second * time_elapsed

    print("\nThat meeting took {0:0.2f} minutes and cost {1:1.2f} {2}. Hope it was worth it! :)".format(
        time_elapsed / 60, cumulative_cost, currency_symbol))


def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        description="A tongue-in-cheek way of tracking the cost of your meetings")
    parser.add_argument("-c", "--currency", dest="currency", action="store", default=DEFAULT_CURRENCY,
                        help="What currency to display (default: {0})".format(DEFAULT_CURRENCY))
    parser.add_argument("-w", "--working-hours", dest="working_hours", action="store", default=DEFAULT_WORKING_HOURS,
                        help="How many working hours in your week? (default: {0})".format(DEFAULT_WORKING_HOURS))

    args = parser.parse_args()
    return args


def print_progress(percent, template):
    print(template.format(percent), end="\r", flush=True)


if __name__ == "__main__":
    main()
