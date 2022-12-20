"""
Author: Rahul Telgote
"""
import sys
import os
sys.path.append(os.getcwd())
import calendar
from sys import argv
from pathlib import Path 
from src.doremi_subscriptions import Subscription
from src.doremi_topups import TopUps
from src.doremi_input_parser import InputParser


class DoReMi:

    def __init__(self, input_data):
        self.input_data = input_data
        self.total_cost = 0
        self.start_date = None
        self.output_data = []
        self.input_parser = InputParser(self.input_data)
        self.date_valid = False
        self.iteration_count = {"MUSIC": 0, "VIDEO": 0, "PODCAST": 0, "TEN_DEVICE": 0, "FOUR_DEVICE": 0}

    def _check_duplicated_input(self):
        subscriptions_duplicated = self.input_parser.subscriptions_duplicated()
        topups_duplicated = self.input_parser.topups_duplicated()
        if subscriptions_duplicated:
            self.output_data.append("ADD_SUBSCRIPTION_FAILED" + " " + subscriptions_duplicated)
        if topups_duplicated:
            self.output_data.append("ADD_TOPUP_FAILED" + " " + topups_duplicated)
        return True

    def _get_subscription_total_cost(self):
        for item in self.input_parser.subscription_orders:
            if self.iteration_count[item["type"]] < 1:
                self.iteration_count[item["type"]] += 1
                subscription_object = Subscription(item["type"], item["plan"], self.start_date)
                if subscription_object.renewal_date == "INVALID_DATE":
                    output = "ADD_SUBSCRIPTION_FAILED" + " " + "INVALID_DATE"
                else:
                    output = "RENEWAL_REMINDER" + " " + item["type"] + " " + subscription_object.renewal_date
                self.total_cost += int(subscription_object.price)
                self.output_data.append(output)

    def _get_subscription_total_cost_with_invalid_date(self):
        for item in self.input_parser.subscription_orders:
            subscription_object = Subscription(item["type"], item["plan"], self.start_date)
            if subscription_object.renewal_date == "INVALID_DATE":
                output = "ADD_SUBSCRIPTION_FAILED" + " " + "INVALID_DATE"
            else:
                output = "RENEWAL_REMINDER" + " " + item["type"] + " " + subscription_object.renewal_date
            self.total_cost += int(subscription_object.price)
            self.output_data.append(output)

    def _get_topup_total_cost_with_invalid_date(self):
        for item in self.input_parser.topups_orders:
            if not self.date_valid:
                self.output_data.append("ADD_TOPUP_FAILED INVALID_DATE")
                continue;
            topup_obj = TopUps(item["type"], item["count"])
            self.total_cost += int(topup_obj.cost)
            self.output_data.append("RENEWAL_AMOUNT" + " " + str(self.total_cost))

    def _get_topup_total_cost(self):
        for item in self.input_parser.topups_orders:
            if self.iteration_count[item["type"]] < 1:
                self.iteration_count[item["type"]] += 1
                if not self.date_valid:
                    self.output_data.append("ADD_TOPUP_FAILED INVALID_DATE")
                    continue;
                topup_obj = TopUps(item["type"], item["count"])
                self.total_cost += int(topup_obj.cost)
                self.output_data.append("RENEWAL_AMOUNT" + " " + str(self.total_cost))

    def print_final_output(self):
        for item in self.output_data:
            print(item)

    def handle_invalid_input(self):
        if not self.date_valid:
            self.output_data = ["INVALID_DATE"] + self.output_data + ['SUBSCRIPTIONS_NOT_FOUND']

    def remove_duplicates_from_output(self):
        pass #self.output_data = list(set(self.output_data))


    def calculate_total_cost(self):
        self.input_parser.parse_inputs()
        self.start_date = self.input_parser.service_start_date
        self.date_valid = self.input_parser.is_date_valid()
        if self.date_valid:
            self._check_duplicated_input()
            self._get_subscription_total_cost()
            self._get_topup_total_cost()
        else:
            self._get_subscription_total_cost_with_invalid_date()
            self._get_topup_total_cost_with_invalid_date()
        self.handle_invalid_input()
        #self.remove_duplicates_from_output()

def main():
    
    """
    Sample code to read inputs from the file"""
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    # file_path = "D:\\DoReMi_GeekTrust\\sample_input\\input1.txt"
    f = open(file_path, 'r')
    lines = f.readlines()
    all_inputs = [inp.strip() for inp in lines]
    do_re_mi = DoReMi(all_inputs)
    do_re_mi.calculate_total_cost()
    do_re_mi.print_final_output()

    
if __name__ == "__main__":
    main()