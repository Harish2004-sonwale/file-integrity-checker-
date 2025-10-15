# hash_generator.py
# Backend module for File Integrity Checker
# Generates SHA256 hash and compares file integrity

import hashlib


def generate_file_hash(file_path):
    """
    Generate SHA256 hash for a given file.
    
    Args:
        file_path (str): Path to the file to hash
        
    Returns:
        str: Hexadecimal SHA256 hash of the file
    """
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to handle large files efficiently
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")


def compare_hashes(original_hash, new_hash):
    """
    Compare two hash values to check file integrity.
    
    Args:
        original_hash (str): Original file hash
        new_hash (str): New file hash to compare
        
    Returns:
        bool: True if hashes match, False otherwise
    """
    return original_hash == new_hash


def get_file_info(file_path):
    """
    Get basic file information.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        dict: File information including size and name
    """
    import os
    
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)
        return {
            "name": file_name,
            "size": file_size,
            "path": file_path
        }
    return None
