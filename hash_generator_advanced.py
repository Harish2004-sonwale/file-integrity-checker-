# hash_generator_advanced.py
# Advanced Backend module for File Integrity Checker
# Supports multiple hash algorithms with progress tracking

import hashlib
import os
import json
from datetime import datetime


def generate_file_hash(file_path, algorithm='sha256', progress_callback=None):
    """
    Generate hash for a given file using specified algorithm.
    
    Args:
        file_path (str): Path to the file to hash
        algorithm (str): Hash algorithm (md5, sha1, sha256, sha512)
        progress_callback (function): Optional callback for progress updates
        
    Returns:
        str: Hexadecimal hash of the file
    """
    # Select hash algorithm
    hash_algorithms = {
        'md5': hashlib.md5(),
        'sha1': hashlib.sha1(),
        'sha256': hashlib.sha256(),
        'sha512': hashlib.sha512()
    }
    
    if algorithm.lower() not in hash_algorithms:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    hash_obj = hash_algorithms[algorithm.lower()]
    
    try:
        file_size = os.path.getsize(file_path)
        bytes_read = 0
        
        with open(file_path, "rb") as f:
            # Read file in chunks to handle large files efficiently
            while True:
                byte_block = f.read(4096)
                if not byte_block:
                    break
                    
                hash_obj.update(byte_block)
                bytes_read += len(byte_block)
                
                # Update progress if callback provided
                if progress_callback and file_size > 0:
                    progress = int((bytes_read / file_size) * 100)
                    progress_callback(progress)
                    
        return hash_obj.hexdigest()
        
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")


def generate_multiple_hashes(file_path, algorithms=['md5', 'sha1', 'sha256', 'sha512'], progress_callback=None):
    """
    Generate multiple hash values for a file.
    
    Args:
        file_path (str): Path to the file
        algorithms (list): List of algorithms to use
        progress_callback (function): Optional callback for progress
        
    Returns:
        dict: Dictionary of algorithm: hash pairs
    """
    results = {}
    total_algorithms = len(algorithms)
    
    for idx, algorithm in enumerate(algorithms):
        try:
            results[algorithm.upper()] = generate_file_hash(file_path, algorithm)
            if progress_callback:
                progress = int(((idx + 1) / total_algorithms) * 100)
                progress_callback(progress)
        except Exception as e:
            results[algorithm.upper()] = f"Error: {str(e)}"
            
    return results


def compare_hashes(original_hash, new_hash):
    """
    Compare two hash values to check file integrity.
    
    Args:
        original_hash (str): Original file hash
        new_hash (str): New file hash to compare
        
    Returns:
        bool: True if hashes match, False otherwise
    """
    return original_hash.lower() == new_hash.lower()


def get_file_info(file_path):
    """
    Get detailed file information.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        dict: File information including size, name, dates
    """
    if os.path.exists(file_path):
        stat_info = os.stat(file_path)
        file_size = stat_info.st_size
        file_name = os.path.basename(file_path)
        
        return {
            "name": file_name,
            "size": file_size,
            "path": file_path,
            "modified": datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            "created": datetime.fromtimestamp(stat_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            "extension": os.path.splitext(file_name)[1]
        }
    return None


def export_hashes_to_file(hash_data, output_file):
    """
    Export hash data to a JSON file.
    
    Args:
        hash_data (dict): Hash data to export
        output_file (str): Path to output file
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(hash_data, f, indent=4)
        return True
    except Exception as e:
        raise Exception(f"Failed to export hashes: {str(e)}")


def import_hashes_from_file(input_file):
    """
    Import hash data from a JSON file.
    
    Args:
        input_file (str): Path to input file
        
    Returns:
        dict: Imported hash data
    """
    try:
        with open(input_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"Failed to import hashes: {str(e)}")


def batch_hash_files(file_paths, algorithm='sha256'):
    """
    Generate hashes for multiple files.
    
    Args:
        file_paths (list): List of file paths
        algorithm (str): Hash algorithm to use
        
    Returns:
        dict: Dictionary of file paths and their hashes
    """
    results = {}
    for file_path in file_paths:
        try:
            results[file_path] = generate_file_hash(file_path, algorithm)
        except Exception as e:
            results[file_path] = f"Error: {str(e)}"
    return results
