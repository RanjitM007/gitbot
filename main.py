import subprocess
from datetime import datetime, timedelta

def git_clone(repo_url, target_folder):
    subprocess.run(['git', 'clone', repo_url, target_folder], check=True)

def git_add_commit_amend_push(repo_path, file_content, commit_message, commit_date):
    try:
        # Change directory to the repository
        subprocess.run(['cd', repo_path], check=True, shell=True)

        # Add file to the staging area
        subprocess.run(['git', 'add', '.'], check=True)

        # Commit the changes
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        # Amend the commit with a specific date
        subprocess.run(['git', 'commit', '--amend', '--date', commit_date], check=True)

        # Force-push the changes to the remote repository
        subprocess.run(['git', 'push', '--force', 'origin', 'main'], check=True)

        print(f"Changes pushed to {repo_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during operations: {e}")

def generate_date_range(start_year, start_month, start_day, end_year, end_month, end_day):
    start_date_str = f"{start_year:04d}-{start_month:02d}-{start_day:02d}"
    end_date_str = f"{end_year:04d}-{end_month:02d}-{end_day:02d}"

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    while start_date <= end_date:
        yield start_date.strftime("%Y-%m-%d")
        start_date += timedelta(days=1)

# Example usage:
repo_url = 'https://github.com/RanjitM007/gitbot.git'
target_folder = 'gitbot_clone'
file_content = 'Hello, world!'
commit_message = 'ranjit'
start_year = 2023
start_month = 12
start_day = 28
end_year = 2023
end_month = 12
end_day = 31

# Clone the repository
git_clone(repo_url, target_folder)

# Add, commit, amend, and push changes for each date in the range
for date_str in generate_date_range(start_year, start_month, start_day, end_year, end_month, end_day):
    commit_date = f"{date_str} 11:12:15"
    # Modify file content for each iteration
    with open(f'{target_folder}/data.txt', 'a') as file:
        file.write(file_content)

    # Perform git operations
    git_add_commit_amend_push(target_folder, file_content, commit_message, commit_date)
