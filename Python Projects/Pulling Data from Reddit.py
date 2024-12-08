import praw  # Library for interacting with the Reddit API
import json  # Library for saving data in JSON format
import os  # Library for file system operations
import re  # Library for regular expressions (regex) processing

# Initialize Reddit API with client credentials
reddit = praw.Reddit(
    client_id=
    client_secret=
    user_agent=
)

# Target URL for the Reddit submission
url = 
submission = reddit.submission(url=url)  # Fetch the Reddit submission

# Load all comments from the submission
submission.comments.replace_more(limit=0)  # Load all comments (limit=0 means no restriction)

# Convert comments to JSONL format
data = []
for comment in submission.comments:
    if comment.body:  # Check if the comment body is not empty
        data.append({
            "prompt": submission.title.strip(),  # Add the submission title as the prompt
            "completion": comment.body.strip()  # Add the comment body as the completion
        })

# Directory where the output file will be saved
output_directory = r"C:\Users\ytuna\OneDrive\Masaüstü\veri"  # Directory path to save the file

# Function to clean invalid characters from the filename
def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)  # Remove invalid characters for Windows filenames

# Create the filename using the cleaned submission title
clean_title = clean_filename(submission.title[:50])  # Limit the title to the first 50 characters
file_name = f"{clean_title}.jsonl"  # Create the filename with .jsonl extension
output_file = os.path.join(output_directory, file_name)  # Full path for the output file

# Create the directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)  

# Write the data to a JSONL file
with open(output_file, "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")  # Write each comment as a JSONL entry

# Print success message
print(f"Comments saved to {output_file}")
