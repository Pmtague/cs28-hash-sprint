def finder(files, queries):

    #Initialize an empty dictionary
    file_paths = {}

    # Loop through files and add file names as keys and file paths as values
    for idx in range (0, len(files)):
        file = files[idx]
        wordlist = file.split("/")
        file_paths[wordlist[-1]] = file
    # Loop through the queries
    for ind in range (0, len(queries)):

    # If the query is in the dictionary
    # Add the value of the query(key) to the result list

    # Return result list 
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
