import os
import sys

import pytest
import logging
import time
import colorlog

from src.ai_client import GeminiClient
from src.judge import AIJudge

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Create the logger
@pytest.fixture
def create_logger():
    name = "app_logger"
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = colorlog.ColoredFormatter(
         '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(log_color)s%(message)s%(reset)s',  # Apply color to entire message
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'blue',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


# Fixture to measure time taken by a test
@pytest.fixture()
def time_tracker(create_logger):
    start_time = time.time()  # Capture the start time
    yield  # This allows the test to run
    end_time = time.time()  # Capture the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    create_logger.info(f"Test completed in {elapsed_time:.4f} seconds.")  # Log the time taken


@pytest.fixture(scope="session")
def gemini_client():
    # Setup: Initialize the client
    client = GeminiClient()

    yield client



@pytest.fixture(scope="session")
def llm_as_judge(gemini_client):
    # Setup: Initialize the client
    judge = AIJudge(gemini_client)

    yield judge
