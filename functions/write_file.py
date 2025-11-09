import os


def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)

        abs_full_path = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)

        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        dir_name = os.path.dirname(abs_full_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        with open(abs_full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"
