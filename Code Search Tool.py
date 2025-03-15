import os
import re

def search_in_file(file_path, pattern, case_sensitive=False):
    """
    Search for a pattern in a file and return matching lines.
    """
    matches = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            if case_sensitive:
                if re.search(pattern, line):
                    matches.append((line_num, line.strip()))
            else:
                if re.search(pattern, line, re.IGNORECASE):
                    matches.append((line_num, line.strip()))
    return matches

def search_in_directory(directory, pattern, file_extensions=None, case_sensitive=False):
    """
    Search for a pattern in all files within a directory.
    """
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file_extensions and not file.endswith(tuple(file_extensions)):
                continue
            file_path = os.path.join(root, file)
            matches = search_in_file(file_path, pattern, case_sensitive)
            if matches:
                results[file_path] = matches
    return results

def display_results(results):
    """
    Display the search results in a readable format.
    """
    for file_path, matches in results.items():
        print(f"\nFile: {file_path}")
        for line_num, line in matches:
            print(f"  Line {line_num}: {line}")

def main():
    # Inputs from the user
    directory = input("Enter directory to search: ").strip()
    pattern = input("Enter search pattern (regex supported): ").strip()
    file_extensions = input("Enter file extensions to search (comma-separated, e.g., .py,.txt): ").strip()
    case_sensitive = input("Case-sensitive search? (y/n): ").strip().lower() == 'y'

    # Process file extensions
    if file_extensions:
        file_extensions = [ext.strip() for ext in file_extensions.split(',')]
    else:
        file_extensions = None

    # Perform the search
    results = search_in_directory(directory, pattern, file_extensions, case_sensitive)

    # Display the results
    if results:
        print("\nSearch Results:")
        display_results(results)
    else:
        print("\nNo matches found.")

if __name__ == "__main__":
    main()