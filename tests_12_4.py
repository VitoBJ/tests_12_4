import logging
import unittest


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    encoding='utf-8',
    filemode='w',
    format='%(levelname)s: %(message)s'
)



class Runner:
    def __init__(self, name: str, speed: float):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if speed <= 0:
            raise ValueError("Speed must be a positive number")
        self.name = name
        self.speed = speed


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("TestRunner", -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')
            self.fail("Expected ValueError for negative speed did not occur")

    def test_run(self):
        try:
            runner = Runner(12345, 10)
        except ValueError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')
            self.fail("Expected ValueError for non-string name did not occur")


if __name__ == '__main__':
    unittest.main()