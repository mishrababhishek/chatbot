from config import config_file
from app.app import run_app
testing = config_file["testing"]

if __name__ == "__main__" and testing:
    import unittest
    from tests import interpreter_test
    runner = unittest.TextTestRunner()
    runner.run(interpreter_test.get_suite())
else: 
    run_app()
