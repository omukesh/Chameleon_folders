import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class RenameHandler(FileSystemEventHandler):
    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.previous_name = None

    def rename_subfolders(self, new_path, old_name, new_name):
        """Renames all subfolders and files recursively."""
        for root, dirs, files in os.walk(new_path, topdown=True):
            for dir_name in dirs:
                if old_name in dir_name:
                    new_dir_name = dir_name.replace(old_name, new_name)
                    os.rename(
                        os.path.join(root, dir_name),
                        os.path.join(root, new_dir_name)
                    )
                    print(f" Renamed Directory: {dir_name} → {new_dir_name}")

            for file_name in files:
                if old_name in file_name:
                    new_file_name = file_name.replace(old_name, new_name)
                    os.rename(
                        os.path.join(root, file_name),
                        os.path.join(root, new_file_name)
                    )
                    print(f" Renamed File: {file_name} → {new_file_name}")

    def on_moved(self, event):
        """Detects folder renames and applies changes inside."""
        if event.is_directory:
            old_path = event.src_path
            new_path = event.dest_path

            old_name = os.path.basename(old_path)
            new_name = os.path.basename(new_path)

            if self.previous_name and old_name != self.previous_name:
                return  # Prevent duplicate triggers

            self.previous_name = new_name  # Store new name
            print(f" Detected rename: {old_name} → {new_name}")

            # Call renaming function
            self.rename_subfolders(new_path, old_name, new_name)
            print(" All nested folders & files renamed successfully.")


if __name__ == "__main__":
    base_directory = "/home/temp2/"  # Adjust this path if needed

    event_handler = RenameHandler(base_directory)
    observer = Observer()
    observer.schedule(event_handler, base_directory, recursive=True)

    print("👀 Monitoring folder renames... Press Ctrl+C to stop.")

    observer.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
