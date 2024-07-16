# Predefined Words Matcher

## Overview

This application is designed to read a plain text file and count occurrences of predefined words specified in another file. It supports the following features:

- **Input Handling**: Reads a plain text file where each line is treated as a separate record.
- **Predefined Words**: Uses a set of predefined words loaded from a separate file (no duplicates).
- **Matching Criteria**: Counts occurrences of each predefined word as whole words in a case-insensitive manner.
- **Output**: Displays the count of each predefined word found in the input file.

### How to Run the Program

1. **Clone the repository**: `git clone <repository_url>`
2. **Navigate to the directory**: `cd <repository_name>`
3. **Install dependencies (if any)**: `pip install -r requirements.txt`
4. **Run the program**: `python main.py <path_to_input_file> <path_to_predefined_words_file>`

```bash
python3 main.py input.txt predefined_words.txt
```
Example Output:
```text
Predefined word     Match count
Name                 2
Detect               0
AI                   1
```

### Assumptions Made

- The predefined words file is correctly formatted and does not contain duplicates.
- Input files (input.txt and predefined_words.txt) are within the specified size limits (up to 20 MB for input files) and are in ASCII format.
- Matching is case-insensitive, meaning "Name" and "name" are considered the same word.
- Words are matched based on exact word boundaries `(\b\w+\b)`, ensuring no partial or substring matches are counted.
- The script operates efficiently within the provided constraints, assuming typical system capabilities for file I/O and memory usage

### Time Complexity Analysis

1. **Reading Files**: 
   - Reading the input file (`input_file`) and the predefined words file (`predefined_words_file`) involves iterating through their content once. Let's denote:
     - `n`: Number of lines in the input file.
     - `m`: Number of words in the predefined words file.
   - Therefore, the complexity for reading these files is O(n + m).

2. **Counting Matches**:
   - For each line in the `text_lines` (from the input file), the script:
     - Splits the line into words (`l` average words per line).
     - Checks each word against the set of predefined words (`k` number of predefined words).
   - The worst-case scenario is iterating through each word in each line and checking against all predefined words.
   - Thus, the complexity for counting matches can be considered as O(n * l * k), where `n` is the number of lines, `l` is the average number of words per line, and `k` is the number of predefined words.

3. **Overall Time Complexity**:
   - Combining the complexities from reading files and counting matches, the overall time complexity is O(n + m + n * l * k). In practical scenarios where `m` is relatively small compared to `n * l * k`, it simplifies to O(n * l * k).

### Space Complexity Analysis

1. **Storage for Input**:
   - Requires space proportional to the size of the input file (`n` lines).

2. **Storage for Predefined Words**:
   - Requires space proportional to the number of predefined words (`k` words).

3. **Additional Data Structures**:
   - Uses a `defaultdict(int)` (`word_count`) to store counts of matched words, which can grow up to the number of unique predefined words (`k`).

Therefore, the space complexity is O(n + m + k), where:
- `n`: Space for storing input lines.
- `m`: Space for storing predefined words.
- `k`: Space for storing counts of matched words.

### What Has Been Tested

- **File Reading**: Ensure the program reads input files correctly.
- **Case Insensitivity**: Verify that matches are case-insensitive.
- **Whole Word Matching**: Confirm that only whole word matches are counted.
- **Edge Cases**: Handles scenarios such as empty files or no matches found. Although not explicitly tested in the provided test case, the script's design implicitly handles these edge cases by default behavior:
    - Empty files would result in no matches.
    - No matches found for predefined words would display a count of 0 for those words.