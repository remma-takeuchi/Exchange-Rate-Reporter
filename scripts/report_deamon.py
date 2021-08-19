#!/usr/bin/env python3
import sys
import time
import daemon
import ex_rate_reporter
import schedule


def job():
    ex_rate_reporter.run()


def main():
    schedule.every().day.at("11:00").do(job)
    schedule.every().day.at("18:00").do(job)
    schedule.every().day.at("22:15").do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
