import os

from config import MAX_FILE_READ_CHARS


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)

        abs_full_path = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)

        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_full_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > MAX_FILE_READ_CHARS:
            content = content[:MAX_FILE_READ_CHARS]
            content += f'\n[...File "{file_path}" truncated at {MAX_FILE_READ_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"
