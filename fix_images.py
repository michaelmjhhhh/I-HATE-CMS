import re
import os
import shutil
import urllib.parse

# Configuration
MARKDOWN_FILE = "/Users/michael/I HATE CMS REPO/I HATE CMS_副本.md"
ASSETS_DIR_NAME = "assets"
MARKDOWN_DIR = os.path.dirname(MARKDOWN_FILE)
ASSETS_DIR_PATH = os.path.join(MARKDOWN_DIR, ASSETS_DIR_NAME)
TARGET_PREFIX = "/Users/michael/Library/Application Support/typora-user-images"

# Create assets directory
if not os.path.exists(ASSETS_DIR_PATH):
    os.makedirs(ASSETS_DIR_PATH)
    print(f"Created directory: {ASSETS_DIR_PATH}")

# Read markdown
with open(MARKDOWN_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_match(match):
    alt_text = match.group(1)
    original_path = match.group(2)
    
    # Check if this is a path we want to replace
    # We look for the typora path prefix
    if TARGET_PREFIX in original_path:
        # Extract filename. 
        # original_path might be URL encoded or raw. 
        # Typora usually writes raw or encoded depending on version. 
        # If it's a file path on disk, we treat it as such.
        # But if it's in markdown `(...)`, it might be encoded.
        # Let's decode it just in case to find the file on disk.
        decoded_path = urllib.parse.unquote(original_path)
        
        # Check if file exists at decoded path
        if os.path.exists(decoded_path):
            filename = os.path.basename(decoded_path)
            dest_path = os.path.join(ASSETS_DIR_PATH, filename)
            
            # Copy file
            if not os.path.exists(dest_path):
                shutil.copy2(decoded_path, dest_path)
                print(f"Copied: {filename}")
            
            # Create new relative path
            # Docusaurus prefers relative paths. 
            # We should URL encode the path for Markdown compliance.
            encoded_filename = urllib.parse.quote(filename)
            new_path = f"./{ASSETS_DIR_NAME}/{encoded_filename}"
            
            return f'![{alt_text}]({new_path})'
        else:
            print(f"Warning: File not found at {decoded_path}")
            return match.group(0)
            
    return match.group(0)

# Regex for markdown images: ![alt](url)
# This simple regex might miss matches with balanced parentheses inside URL, but standard image links are usually simple.
image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
new_content = image_pattern.sub(replace_match, content)

with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Finished processing markdown file.")
