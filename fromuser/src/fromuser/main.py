#!/usr/bin/env python
import sys
import warnings
import json
import os


from datetime import datetime

from fromuser.crew import Fromuser

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def setup_directories():
    """Create necessary directories if they don't exist"""
    os.makedirs("outputs", exist_ok=True)

def get_user_input():
    """
    Get user inputs interactively.
    """
    print("Please provide the following information to generate your user profile:")
    print("----------------------------------------------------------------------")
    
    user_name = input("Full Name: ")
    user_email = input("Email Address: ")
    educational_background = input("Educational Background (e.g., degrees, institutions): ")
    professional_background = input("Professional Background (e.g., work experience, roles): ")
    skills = input("Skills (comma-separated list): ")
    github_username = input("GitHub Username: ")
    linkedin_url = input("LinkedIn URL or Username: ")
    medium_username = input("Medium Username: ")
    
    # Format LinkedIn URL if only username was provided
    if linkedin_url and not linkedin_url.startswith("http"):
        linkedin_url = f"https://linkedin.com/in/{linkedin_url}"
    
    return {
        'user_name': user_name,
        'user_email': user_email,
        'educational_background': educational_background,
        'professional_background': professional_background,
        'skills': skills,
        'github_username': github_username,
        'linkedin_url': linkedin_url,
        'medium_username': medium_username,
        'current_year': str(datetime.now().year)
    }

def run():
    """
    Run the crew to generate a comprehensive user profile.
    """
    # Setup output directory
    setup_directories()
    
    # Get user inputs
    inputs = get_user_input()
    
    print("\nGenerating your comprehensive user profile. This may take some time...")
    
    try:
        # Run the crew with the provided inputs
        result = Fromuser().crew().kickoff(inputs=inputs)
        print(f"\nUser profile generation completed. Results saved to 'user_persona.json'")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Get user inputs
    inputs = get_user_input()
    
    try:
        Fromuser().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Fromuser().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    # Get user inputs
    inputs = get_user_input()
    
    try:
        results = Fromuser().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
        return results
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    # If the script is run directly, execute the run function
    run()
