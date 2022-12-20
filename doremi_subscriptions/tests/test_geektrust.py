import sys
import os
import unittest

project_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_dir)

from geektrust import DoReMi
output_dir = os.path.join(project_dir, "tests", "sample_output")
input_dir = os.path.join(project_dir, "tests", "sample_input")


class FooTest2(unittest.TestCase):

	def get_parsed_data_from_file(self, file_path):
		all_inputs = []
		with open(file_path, 'r') as file_handler:
			lines = file_handler.readlines()
			all_inputs = [inp.strip() for inp in lines]
		return all_inputs

	def test_calculate_cost_with_correct_input(self):
		sample_input = self.get_parsed_data_from_file(os.path.join(input_dir, "input1.txt"))
		sample_output = self.get_parsed_data_from_file(os.path.join(output_dir, "output1.txt"))
		doremi_obj = DoReMi(sample_input)
		doremi_obj.calculate_total_cost()
		for idx in range(len(doremi_obj.output_data)):
			assert doremi_obj.output_data[idx] == sample_output[idx]

	def test_calculate_cost_without_video_input(self):
		sample_input = self.get_parsed_data_from_file(os.path.join(input_dir, "input2.txt"))
		sample_output = self.get_parsed_data_from_file(os.path.join(output_dir, "output2.txt"))
		doremi_obj = DoReMi(sample_input)
		doremi_obj.calculate_total_cost()
		for idx in range(len(doremi_obj.output_data)):
			assert doremi_obj.output_data[idx] == sample_output[idx]

	def test_calculate_cost_without_topup_input(self):
		sample_input = self.get_parsed_data_from_file(os.path.join(input_dir, "input3.txt"))
		sample_output = self.get_parsed_data_from_file(os.path.join(output_dir, "output3.txt"))
		doremi_obj = DoReMi(sample_input)
		doremi_obj.calculate_total_cost()
		for idx in range(len(doremi_obj.output_data)):
			assert doremi_obj.output_data[idx] == sample_output[idx]

	def test_calculate_cost_with_invalid_date(self):
		sample_input = self.get_parsed_data_from_file(os.path.join(input_dir, "input4.txt"))
		sample_output = self.get_parsed_data_from_file(os.path.join(output_dir, "output4.txt"))
		doremi_obj = DoReMi(sample_input)
		doremi_obj.calculate_total_cost()
		for idx in range(len(doremi_obj.output_data)):
			assert doremi_obj.output_data[idx] == sample_output[idx]

	def test_calculate_cost_with_duplicate_category(self):
		sample_input = self.get_parsed_data_from_file(os.path.join(input_dir, "input5.txt"))
		sample_output = self.get_parsed_data_from_file(os.path.join(output_dir, "output5.txt"))
		doremi_obj = DoReMi(sample_input)
		doremi_obj.calculate_total_cost()
		for idx in range(len(doremi_obj.output_data)):
			assert doremi_obj.output_data[idx] == sample_output[idx]

if __name__ == '__main__':
    unittest.main()