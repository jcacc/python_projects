import os
import glob
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser

# Define the directory path where the text files are located
directory_path = "/data/itysl.txt"

# Define the directory path where the Whoosh index will be created
index_directory_path = "/data/"

# Define the schema for the index
schema = Schema(id=ID(unique=True, stored=True), content=TEXT(stored=True))

# Create the index
if not os.path.exists(index_directory_path):
    os.mkdir(index_directory_path)
    ix = create_in(index_directory_path, schema)
else:
    ix = create_in(index_directory_path, schema, True)

# Get a list of all the text files in the directory
text_files = glob.glob(directory_path + "*.txt")

# Open each text file, extract the lines of text, and add them to the index
with ix.writer() as writer:
    for text_file in text_files:
        with open(text_file, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                writer.add_document(id=text_file + "_" + str(i), content=line)

# Search the index for a query
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("search query")
    results = searcher.search(query)
    for result in results:
        print(result['id'], result['content'])
