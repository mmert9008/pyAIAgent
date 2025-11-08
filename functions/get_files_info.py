import os


def get_files_info(working_directory, directory="."):
    try:
        # Create the full path by joining working_directory and directory
        full_path = os.path.join(working_directory, directory)

        # Get absolute paths to ensure we're comparing normalized paths
        abs_full_path = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)

        # Check if the target directory is within the working directory
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if the path is actually a directory
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        # List the contents of the directory
        entries = os.listdir(abs_full_path)

        # Build the output string
        result_lines = []
        for entry in entries:
            entry_path = os.path.join(abs_full_path, entry)
            file_size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            result_lines.append(
                f" - {entry}: file_size={file_size} bytes, is_dir={is_dir}"
            )

        return "\n".join(result_lines)

    except Exception as e:
        return f"Error: {str(e)}"
