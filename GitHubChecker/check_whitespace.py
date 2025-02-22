import requests

repo_owner = input("Please enter the repo owners name")
repo_name = input("Please enter the repo name")

BASE_URL = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"



def get_python_files(path=""):
    url = f"{BASE_URL}/{path}" if path else BASE_URL
    response = requests.get(url)
    response.raise_for_status()
    files = response.json()
    python_files = []

    for file in files:
        if file["type"] == "file" and file["name"].endswith(".py"):
            python_files.append(file["download_url"])
        elif file["type"] == "dir":
            python_files.extend(get_python_files(file["path"]))

    return python_files


def check_whitespace_in_file(file_url, max_spaces = 10):
    response = requests.get(file_url)
    response.raise_for_status()
    lines = response.text.splitlines()
    excessive_whitespace_lines = []
    for idx, line in enumerate(lines, start=1):
        leading_spaces = len(line) - len(line.lstrip())
        if leading_spaces > max_spaces:
            excessive_whitespace_lines.append((idx, leading_spaces, line.strip()))

    return excessive_whitespace_lines

def check_all_python_files():
    python_files = get_python_files()
    for file_url in python_files:
        excessive_lines = check_whitespace_in_file(file_url)
        if excessive_lines:
            print(f'In file {file_url}:')
            for line_num, spaces, line in excessive_lines:
                print(f'Line {line_num} - {spaces} spaces: {line}')

if __name__ == '__main__':
    check_all_python_files()
