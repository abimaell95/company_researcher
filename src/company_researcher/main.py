#!/usr/bin/env python
from company_researcher.crew import CompanyResearchCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'company': 'Apple.com'
    }
    CompanyResearchCrew().crew().kickoff(inputs=inputs)