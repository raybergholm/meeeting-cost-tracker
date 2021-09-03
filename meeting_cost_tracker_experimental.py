#!/usr/bin/env python3

import argparse
import datetime
import time
import keyboard

DEFAULT_SALARY = "4500" 
DEFAULT_PARTICIPANT_COUNT = "2"
DEFAULT_REFRESH_RATE = "0.5"
DEFAULT_CURRENCY_SYMBOL = "euros"

def main():
    args = parse_cli_arguments()
    participants = int(args.participant_count)

    average_salary = float(args.average_salary)
    working_hours_per_week = 37.5
    cost_per_second = (average_salary/(4*working_hours_per_week))/3600

    refresh_rate = float(args.refresh_rate)

    currency_symbol = args.currency_symbol

    tick_rate = cost_per_second / refresh_rate
    
    start_time = time.time()
    end_time = None
    time_elapsed = None
    cumulative_cost = 0.0

    # print("Meeting started at {0}".format(datetime.time()("%d.%m %I:%M:%s %p")))
    exit = False
    while not exit:
        if keyboard.is_pressed("esc"):
            print("EXITING NOW")
            exit = True
        
        # if keyboard.is_pressed("+") or keyboard.is_pressed(">"):
        #     participants = participants + 1

        # if keyboard.is_pressed("-") or keyboard.is_pressed("<"):
        #     participants = participants - 1

        cumulative_cost = cumulative_cost + (participants * tick_rate)
        time_elapsed = time.time() - start_time
        # print("Seconds elapsed: {0}\nCost incurred: {1:1.2f} {2}\nCurrent number of participants: {3}\n".format(time_elapsed, cumulative_cost, currency_symbol, participants), end="\r", flush=True)
        output_string = "Cost incurred: {0:0.2f} {1}".format(cumulative_cost, currency_symbol)
        print(output_string, end="\r", flush=True)


        time.sleep(refresh_rate)
        
    
    end_time = time.time()
    print("Meeting finished at {0}".format(end_time))
    print("That meeting took {:0.2f} minutes and cost {:0.2f}€. Hope it was worth it! :)".format(time_elapsed / 60, cumulative_cost))

def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        description="A tongue-in-cheek way of tracking the cost of your meetings")
    parser.add_argument("-m", "--average-salary", dest="average_salary", action="store", default=DEFAULT_SALARY,
                        help="Average minute rate of participants (default: {0})".format(DEFAULT_SALARY))
    parser.add_argument("-p", "--participant-count", dest="participant_count", action="store", default=DEFAULT_PARTICIPANT_COUNT,
                        help="Number of participants (default: {0}). Increase or decrease this value on the fly with + / > or - / <".format(DEFAULT_PARTICIPANT_COUNT))
    parser.add_argument("-r", "--refresh-rate", dest="refresh_rate", action="store", default=DEFAULT_REFRESH_RATE,
                        help="How often to update the screen in seconds (default: {0})".format(DEFAULT_REFRESH_RATE))
    parser.add_argument("-c", "--currency-symbol", dest="currency_symbol", action="store", default=DEFAULT_CURRENCY_SYMBOL,
                        help="Currency symbol to display (default: {0})".format(DEFAULT_CURRENCY_SYMBOL))

    args = parser.parse_args()
    return args

def print_progress(percent, template):
    print(template.format(percent), end="\r", flush=True)

if __name__ == "__main__":
    main()