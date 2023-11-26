import requests
import logging
import os

# Configure logging
logging.basicConfig(filename=f'{os.path.expanduser("~")}/deployments/cicd_deployment/deploy.log', 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')

# GitHub API parameters
repo = 'LeftAttention/cicd_assignment'
file_path = 'index.html'
url = f'https://api.github.com/repos/{repo}/commits?path={file_path}'

def get_last_commit_id():
    try:
        with open(f'{os.path.expanduser("~")}/deployments/cicd_deployment/last_commit_id.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
    
def set_last_commit_id(commit_id):
    with open(f'{os.path.expanduser("~")}/deployments/cicd_deployment/last_commit_id.txt', 'w') as file:
        file.write(commit_id)

def has_new_commit():
    response = requests.get(url)
    logging.info("Fetching new commits.")
    if response.status_code == 200:
        commits = response.json()
        if commits:
            latest_commit = commits[0]
            commit_id = latest_commit['sha']
            author = latest_commit['commit']['author']['name']
            commit_time = latest_commit['commit']['author']['date']
            message = latest_commit['commit']['message']

            # Check if the latest commit SHA is different from the last stored one
            prev_commit_id = get_last_commit_id()
            if commit_id != prev_commit_id:
                set_last_commit_id(commit_id)
                # Log the commit details
                logging.info(f"New commit by {author} at {commit_time}: {commit_id} - {message}")
                return True
            else:
                logging.info(f"No new commit found. The last commit id was {commit_id}")
    else:
        logging.error('Failed to fetch commits')
    return False

if __name__ == '__main__':
    if has_new_commit():
        logging.info("Running the deployment script")
        os.system(f'bash {os.path.expanduser("~")}/deployments/cicd_deployment/deploy.sh')