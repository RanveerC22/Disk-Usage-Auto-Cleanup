import subprocess
import shutil
import os

def get_filesystem_usage(filesystem):
    try:
        # Execute 'df -h' and get output
        result = subprocess.run(["df", "-h", filesystem], capture_output=True, text=True, check=True)
        
        # Print the output for visibility
        print(f"Disk Usage for {filesystem}:")
        print(result.stdout.strip())

        # Parse the output to get the usage percentage
        output_lines = result.stdout.strip().split("\n")
        usage_line = output_lines[1]  # The second line contains the details
        usage_percent = int(usage_line.split()[4].replace("%", ""))  # Extract usage percentage
        
        return usage_percent
    except Exception as e:
        print(f"Error checking filesystem usage: {e}")
        return None

def delete_folders_in_directory(directory):
    try:
        if os.path.exists(directory):
            print(f"Deleting folders in directory: {directory}")
            for folder in os.listdir(directory):
                folder_path = os.path.join(directory, folder)
                if os.path.isdir(folder_path):
                    print(f"Deleting folder: {folder_path}")
                    shutil.rmtree(folder_path)  # Deletes the folder and its contents
            print("All eligible folders deleted successfully.")
        else:
            print(f"Directory {directory} does not exist.")
    except Exception as e:
        print(f"Error deleting folders: {e}")

if __name__ == "__main__":
    filesystem = "/dev/mapper/ubuntu--vg-ubuntu--lv"
    target_directory = "/opt/buildAgent/work/.old"
    
    # Check filesystem usage before deletion
    print("\n--- Checking Disk Space BEFORE Deletion ---")
    usage_before = get_filesystem_usage(filesystem)

    if usage_before is not None:
        print(f"\nUsage of {filesystem}: {usage_before}%")
        if usage_before > 70:
            print(f"\nDisk usage exceeds 70%. Proceeding to delete folders in {target_directory}...\n")
            delete_folders_in_directory(target_directory)
            
            # Check filesystem usage after deletion
            print("\n--- Checking Disk Space AFTER Deletion ---")
            usage_after = get_filesystem_usage(filesystem)
            print(f"\nUsage of {filesystem} AFTER Deletion: {usage_after}%")
        else:
            print(f"\nUsage is below 70% ({usage_before}%). No action taken.")
    else:
        print("\nFailed to retrieve filesystem usage.")
