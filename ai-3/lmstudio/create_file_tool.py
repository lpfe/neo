from pathlib import Path

def create_file(name : str, content : str) :
    """
    Create a new file with the given name and write the specified content into it.
    If the file already exists, return an error message.
    """
    dest_path = Path(name)
    if dest_path.exists() :
        return "Error : File already exists"
    try :
        dest_path.write_text(content, encoding = "utf-8")
    except Exception as e :
        return f"Error : {e!r}"
    return f"File created"