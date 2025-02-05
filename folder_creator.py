import os


def create_project_structure(base_directory, project_name):
    """ Creates a project folder structure dynamically. """

    # Define the folder structure
    subfolders = {
        f"{project_name}_Data": ["Input", "Logs", "Output"],
        f"{project_name}_Reports": ["Finance", "Revenues", "Expenditure"],
        f"{project_name}_Scripts": ["Robots", "PLC", "Vision"],
        f"{project_name}_Resources": ["Logs", "Materials", "Business_Cards"]
    }

    # Create the main project folder
    project_path = os.path.join(base_directory, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Create subfolders and their internal structure
    for folder, sub_dirs in subfolders.items():
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for sub_dir in sub_dirs:
            os.makedirs(os.path.join(folder_path, f"{folder}_{sub_dir}"), exist_ok=True)

    print(f" Folder structure for '{project_name}' created successfully at {project_path}")


if __name__ == "__main__":
    base_directory = "/home/mukesh/temp2"  # Change this to your base directory
    project_name = input("Enter Project Name: ")  # Change to your project name

    create_project_structure(base_directory, project_name)
