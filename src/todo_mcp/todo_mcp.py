# import libraries
from fastmcp import FastMCP
from typing import Annotated
from todo_mcp.todo_db import TodoDB

#Create the DB 
todo_db = TodoDB(db_file='/Users/linjiawei/Desktop/Folders/GeeksHacking/geekshacking-mcp/todo_db.json')
#todo_db.sample_data()

# Create the MCP server
mcp = FastMCP('todo_mcp')

# Tools
@mcp.tool(
    name="tool_add_todo",
    description="Add a single #TODO text from a source file"
)
def add_todo(
        filename: Annotated[str, "Source file containing the #ToDO"],
        line_num: Annotated[int, "Line number of the #TODO"],
        text: Annotated[str, "#ToDO text to add"],
):
    return todo_db.add(filename, text, line_num)

# Resource
@mcp.resource(
        name="resource_get_todos_for_file",
        description="Get all #TODO texts for a source file. Returns an empty array if source files does not exists or there are no #TODO from the file",
        uri="todo://{filename}/todos"
)
def get_todos_for_file(
        filename: Annotated[str, "Source file containing the #TODO"]
):
    todos = todo_db.get(filename)
    return [ text for text in todos.values() ]

# Start the MCP
def main():
    mcp.run()

if __name__ == "__main__":
    main()