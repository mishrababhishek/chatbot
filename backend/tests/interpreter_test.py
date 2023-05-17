from models.interpreter import Interpreter
from data import data
import os
import unittest

class InterpreterTest(unittest.TestCase):
    def test_train_and_save_model(self):
        Interpreter.create_new_interpreter("default")
        all_files = os.listdir("models/saved")
        passed = True if "test.json" in all_files else False
        self.assertEqual(passed, True, "Successfully Trained and Saved Model")
    
    def test_load_trained_model(self):
        interpreter = None
        interpreter = Interpreter.load_interpreter("default")
        self.assertIsNot(interpreter, None, "Successfully Loaded Model")

    def test_response_on_dataset(self):
        interpreter = Interpreter.load_interpreter("default")
        querys = data.querys
        for i, query in enumerate(querys):
            with self.subTest(case=i):
                for question in query["questions"]:
                    response = interpreter.parse(question)
                    self.assertEqual(response, query["intent"], f"Response To {question} is {query['intent']}")


def get_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        InterpreterTest("test_train_and_save_model"),
        InterpreterTest("test_load_trained_model"),
        InterpreterTest("test_response_on_dataset")
    ])
    return suite