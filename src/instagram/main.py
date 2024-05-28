#!/usr/bin/env python
from instagram.crew import InstagramCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    InstagramCrew().crew().kickoff(inputs=inputs)