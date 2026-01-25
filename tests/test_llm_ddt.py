import sys

import pytest
import os
import csv
import src
from src.ai_client import GeminiClient
from src.judge import AIJudge


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



def load_data():
    with open("data/promts.csv", mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        reader = csv.DictReader(lines, delimiter=';')
        res = [row for row in reader]
        return res

@pytest.mark.parametrize("case", load_data())
def test_ai_response_quality(case, time_tracker):
    client = GeminiClient()
    judge = AIJudge(client)

    actual_response = client.ask(case['user_prompt'])

    result = judge.evaluate(case["user_prompt"],actual_response, case['acceptance_criteria'])
    assert result['verdict'] == "PASS", f"Judge failed it:{result['reason']}"


def test_ai_first(time_tracker):
    client = GeminiClient()
    judge = AIJudge(client)
    actual_response = client.ask('What are the most useful features in Pytest? Answer in 2 sentence')
    evaluation = judge.evaluate('What are the most useful features in Pytest? Answer in 2 sentence', actual_response,
                                "The answer should accurately highlight Pytest's most useful features, such as its simplicity, fixture support, built-in assertions, and ability to run tests in parallel, while remaining concise, clear, and free from unnecessary details or examples, all within exactly two sentences.")
    assert evaluation['verdict'] == "PASS", f"Judge failed it:{evaluation['reason']}"



