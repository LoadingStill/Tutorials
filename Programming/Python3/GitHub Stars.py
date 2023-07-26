#To count the stars in a user's GitHub repository, we will need to use the GitHub API.
#In Python, we can use the requests library to make HTTP requests to the API and get the necessary data.
#Here's a Python program that prompts the user for their GitHub username and then counts the number of stars in all their repositories:
#In this program, we first prompt the user for their GitHub username.
#We then make a request to the GitHub API to get a list of all the user's repositories.
#We check if the request was successful, and if it was, we loop through the list of repositories and add up the number of stars in each one.
#Finally, we print out the total number of stars in all the user's repositories.



import requests

# Prompt the user for their GitHub username
username = input("Enter your GitHub username: ")

# Make a request to the GitHub API to get the user's repositories
response = requests.get(f"https://api.github.com/users/{username}/repos")

# Check if the request was successful
if response.status_code != 200:
    print("Error: Failed to retrieve repositories.")
    exit()

# Count the number of stars in all the user's repositories
star_count = 0
for repo in response.json():
    star_count += repo["stargazers_count"]

# Print the total number of stars
print(f"Total number of stars in {username}'s repositories: {star_count}")
