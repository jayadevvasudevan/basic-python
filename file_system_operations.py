"""
File System Operations
Comprehensive file and directory management utilities.
Demonstrates path manipulation, file operations, directory traversal, and more.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Optional


class FileSystemManager:
    """Utility class for file system operations."""
    
    @staticmethod
    def create_directory(path: str, exist_ok: bool = True):
        """
        Create a directory and all parent directories.
        
        Args:
            path: Directory path to create
            exist_ok: Don't raise error if directory exists
        """
        try:
            Path(path).mkdir(parents=True, exist_ok=exist_ok)
            print(f"✓ Directory created: {path}")
        except FileExistsError:
            print(f"✗ Directory already exists: {path}")
        except Exception as e:
            print(f"✗ Error creating directory: {e}")
    
    @staticmethod
    def list_files(directory: str, extension: Optional[str] = None, 
                   recursive: bool = False) -> List[str]:
        """
        List all files in a directory.
        
        Args:
            directory: Directory to list files from
            extension: Filter by file extension (e.g., '.txt')
            recursive: Search subdirectories recursively
        
        Returns:
            List of file paths
        """
        files = []
        dir_path = Path(directory)
        
        if not dir_path.exists():
            print(f"Directory does not exist: {directory}")
            return files
        
        if recursive:
            pattern = f"**/*{extension}" if extension else "**/*"
            files = [str(f) for f in dir_path.glob(pattern) if f.is_file()]
        else:
            pattern = f"*{extension}" if extension else "*"
            files = [str(f) for f in dir_path.glob(pattern) if f.is_file()]
        
        return files
    
    @staticmethod
    def get_file_info(filepath: str) -> dict:
        """
        Get detailed information about a file.
        
        Args:
            filepath: Path to the file
        
        Returns:
            Dictionary with file information
        """
        path = Path(filepath)
        
        if not path.exists():
            return {"error": "File does not exist"}
        
        stats = path.stat()
        
        return {
            "name": path.name,
            "path": str(path.absolute()),
            "size_bytes": stats.st_size,
            "size_mb": round(stats.st_size / (1024 * 1024), 2),
            "created": datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
            "modified": datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
            "extension": path.suffix,
            "is_file": path.is_file(),
            "is_dir": path.is_dir()
        }
    
    @staticmethod
    def copy_file(source: str, destination: str, overwrite: bool = False):
        """
        Copy a file to a destination.
        
        Args:
            source: Source file path
            destination: Destination file path
            overwrite: Whether to overwrite existing file
        """
        src_path = Path(source)
        dst_path = Path(destination)
        
        if not src_path.exists():
            print(f"✗ Source file does not exist: {source}")
            return
        
        if dst_path.exists() and not overwrite:
            print(f"✗ Destination exists (use overwrite=True): {destination}")
            return
        
        try:
            shutil.copy2(source, destination)
            print(f"✓ File copied: {source} → {destination}")
        except Exception as e:
            print(f"✗ Error copying file: {e}")
    
    @staticmethod
    def move_file(source: str, destination: str):
        """
        Move a file to a new location.
        
        Args:
            source: Source file path
            destination: Destination file path
        """
        try:
            shutil.move(source, destination)
            print(f"✓ File moved: {source} → {destination}")
        except Exception as e:
            print(f"✗ Error moving file: {e}")
    
    @staticmethod
    def delete_file(filepath: str, confirm: bool = True):
        """
        Delete a file.
        
        Args:
            filepath: Path to file to delete
            confirm: Ask for confirmation before deleting
        """
        path = Path(filepath)
        
        if not path.exists():
            print(f"✗ File does not exist: {filepath}")
            return
        
        if confirm:
            response = input(f"Delete {filepath}? (yes/no): ").lower()
            if response != 'yes':
                print("Deletion cancelled")
                return
        
        try:
            path.unlink()
            print(f"✓ File deleted: {filepath}")
        except Exception as e:
            print(f"✗ Error deleting file: {e}")
    
    @staticmethod
    def get_directory_size(directory: str) -> Tuple[int, int]:
        """
        Calculate total size of all files in a directory.
        
        Args:
            directory: Directory path
        
        Returns:
            Tuple of (total_size_bytes, file_count)
        """
        total_size = 0
        file_count = 0
        
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)
                    file_count += 1
                except (OSError, FileNotFoundError):
                    continue
        
        return total_size, file_count
    
    @staticmethod
    def search_files(directory: str, pattern: str, case_sensitive: bool = False) -> List[str]:
        """
        Search for files matching a pattern in their name.
        
        Args:
            directory: Directory to search
            pattern: Pattern to match in filename
            case_sensitive: Whether search is case-sensitive
        
        Returns:
            List of matching file paths
        """
        matches = []
        dir_path = Path(directory)
        
        if not dir_path.exists():
            return matches
        
        for file in dir_path.rglob("*"):
            if file.is_file():
                filename = file.name if case_sensitive else file.name.lower()
                search_pattern = pattern if case_sensitive else pattern.lower()
                
                if search_pattern in filename:
                    matches.append(str(file))
        
        return matches
    
    @staticmethod
    def organize_files_by_extension(directory: str, dry_run: bool = True):
        """
        Organize files in a directory by creating folders for each extension.
        
        Args:
            directory: Directory to organize
            dry_run: If True, only show what would be done
        """
        dir_path = Path(directory)
        
        if not dir_path.exists():
            print(f"Directory does not exist: {directory}")
            return
        
        files = [f for f in dir_path.iterdir() if f.is_file()]
        
        # Group files by extension
        extensions = {}
        for file in files:
            ext = file.suffix.lower() or 'no_extension'
            if ext not in extensions:
                extensions[ext] = []
            extensions[ext].append(file)
        
        # Show or perform organization
        for ext, file_list in extensions.items():
            folder_name = ext.replace('.', '') if ext != 'no_extension' else ext
            target_folder = dir_path / folder_name
            
            print(f"\n{ext.upper()} files → {folder_name}/ folder:")
            
            if not dry_run:
                target_folder.mkdir(exist_ok=True)
            
            for file in file_list:
                target_path = target_folder / file.name
                print(f"  {'[DRY RUN]' if dry_run else '✓'} {file.name}")
                
                if not dry_run:
                    file.rename(target_path)
        
        if dry_run:
            print("\nThis was a dry run. Set dry_run=False to perform the operation.")


# Example usage and demonstrations
def demonstrate_file_operations():
    """Demonstrate various file system operations."""
    
    print("=" * 70)
    print("File System Operations - Demonstrations")
    print("=" * 70)
    
    # 1. Get current working directory
    print("\n1. Current Working Directory:")
    print("-" * 70)
    cwd = Path.cwd()
    print(f"Current directory: {cwd}")
    
    # 2. Path manipulation
    print("\n2. Path Manipulation:")
    print("-" * 70)
    
    example_path = Path("folder/subfolder/file.txt")
    print(f"Original path: {example_path}")
    print(f"Parent directory: {example_path.parent}")
    print(f"Filename: {example_path.name}")
    print(f"Stem (without extension): {example_path.stem}")
    print(f"Extension: {example_path.suffix}")
    print(f"Absolute path: {example_path.absolute()}")
    
    # 3. Check file existence
    print("\n3. File Existence Checks:")
    print("-" * 70)
    
    test_file = Path(__file__)  # This script itself
    print(f"File: {test_file.name}")
    print(f"Exists: {test_file.exists()}")
    print(f"Is file: {test_file.is_file()}")
    print(f"Is directory: {test_file.is_dir()}")
    
    # 4. Get file information
    print("\n4. File Information:")
    print("-" * 70)
    
    info = FileSystemManager.get_file_info(__file__)
    for key, value in info.items():
        print(f"{key}: {value}")
    
    # 5. List files in current directory
    print("\n5. List Python Files in Current Directory:")
    print("-" * 70)
    
    py_files = FileSystemManager.list_files(".", extension=".py", recursive=False)
    for i, file in enumerate(py_files[:5], 1):  # Show first 5
        print(f"{i}. {Path(file).name}")
    if len(py_files) > 5:
        print(f"... and {len(py_files) - 5} more files")
    
    # 6. Calculate directory size
    print("\n6. Directory Size Calculation:")
    print("-" * 70)
    
    total_size, file_count = FileSystemManager.get_directory_size(".")
    size_mb = round(total_size / (1024 * 1024), 2)
    print(f"Total files: {file_count}")
    print(f"Total size: {size_mb} MB ({total_size:,} bytes)")
    
    # 7. Path joining
    print("\n7. Safe Path Joining:")
    print("-" * 70)
    
    base = Path("projects")
    sub = "python"
    filename = "script.py"
    full_path = base / sub / filename
    print(f"Joined path: {full_path}")
    
    # 8. File extension operations
    print("\n8. File Extension Operations:")
    print("-" * 70)
    
    files_by_ext = {}
    for file in FileSystemManager.list_files(".", recursive=False):
        ext = Path(file).suffix or "no extension"
        files_by_ext[ext] = files_by_ext.get(ext, 0) + 1
    
    print("Files by extension:")
    for ext, count in sorted(files_by_ext.items()):
        print(f"  {ext}: {count} file(s)")
    
    # 9. Demonstrate path resolution
    print("\n9. Path Resolution:")
    print("-" * 70)
    
    relative_path = Path("./folder/../file.txt")
    print(f"Relative: {relative_path}")
    print(f"Resolved: {relative_path.resolve()}")


if __name__ == "__main__":
    demonstrate_file_operations()
