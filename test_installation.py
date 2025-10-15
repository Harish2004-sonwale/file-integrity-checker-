#!/usr/bin/env python3
"""
Test Installation Script for File Integrity Checker
Run this script to verify all dependencies are correctly installed.
"""

import sys
import os


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_status(message, status):
    """Print a status message with color coding"""
    if status == "OK":
        print(f"[OK]   {message}: {status}")
    elif status == "FAIL":
        print(f"[FAIL] {message}: {status}")
    else:
        print(f"[INFO] {message}: {status}")


def test_python_version():
    """Test Python version"""
    print_header("Testing Python Version")
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 6:
        print_status("Python Version", "OK")
        return True
    else:
        print_status("Python Version", "FAIL")
        print("[WARNING] Python 3.6+ required!")
        return False


def test_imports():
    """Test required module imports"""
    print_header("Testing Required Modules")
    
    modules = {
        "hashlib": False,
        "tkinter": False,
        "os": False,
    }
    
    # Test hashlib
    try:
        import hashlib
        modules["hashlib"] = True
        print_status("hashlib (SHA256 hashing)", "OK")
    except ImportError:
        print_status("hashlib (SHA256 hashing)", "FAIL")
    
    # Test tkinter
    try:
        import tkinter as tk
        root = tk.Tk()
        root.destroy()
        modules["tkinter"] = True
        print_status("tkinter (GUI framework)", "OK")
    except ImportError:
        print_status("tkinter (GUI framework)", "FAIL")
        print("[WARNING] Install Tkinter: sudo apt-get install python3-tk (Linux)")
    except Exception as e:
        print_status("tkinter (GUI framework)", "FAIL")
        print(f"[WARNING] Error: {e}")
    
    # Test os
    try:
        import os
        modules["os"] = True
        print_status("os (file operations)", "OK")
    except ImportError:
        modules["os"] = False
        print_status("os (file operations)", "FAIL")
    
    return all(modules.values())


def test_project_files():
    """Test if project files exist"""
    print_header("Testing Project Files")
    
    files = {
        "hash_generator.py": False,
        "app_gui.py": False,
        "README.md": False,
        "PROJECT_REPORT.md": False,
        "USAGE_GUIDE.md": False,
    }
    
    for filename in files.keys():
        if os.path.exists(filename):
            files[filename] = True
            print_status(filename, "OK")
        else:
            print_status(filename, "FAIL")
    
    return all(files.values())


def test_hash_generation():
    """Test hash generation functionality"""
    print_header("Testing Hash Generation")
    
    try:
        # Create a temporary test file
        test_file = "temp_test_file.txt"
        test_content = "This is a test file for hash generation."
        
        with open(test_file, "w") as f:
            f.write(test_content)
        
        print(f"Created test file: {test_file}")
        
        # Import and test hash generation
        from hash_generator import generate_file_hash, compare_hashes
        
        # Generate hash
        hash1 = generate_file_hash(test_file)
        print(f"Generated hash: {hash1[:32]}...")
        print_status("Hash generation", "OK")
        
        # Test comparison (same file)
        hash2 = generate_file_hash(test_file)
        if compare_hashes(hash1, hash2):
            print_status("Hash comparison (same file)", "OK")
        else:
            print_status("Hash comparison (same file)", "FAIL")
            return False
        
        # Modify file and test again
        with open(test_file, "a") as f:
            f.write(" Modified!")
        
        hash3 = generate_file_hash(test_file)
        if not compare_hashes(hash1, hash3):
            print_status("Hash comparison (modified file)", "OK")
        else:
            print_status("Hash comparison (modified file)", "FAIL")
            return False
        
        # Cleanup
        os.remove(test_file)
        print(f"Cleaned up test file: {test_file}")
        
        return True
        
    except Exception as e:
        print_status("Hash generation", "FAIL")
        print(f"[WARNING] Error: {e}")
        # Cleanup on error
        if os.path.exists(test_file):
            os.remove(test_file)
        return False


def run_all_tests():
    """Run all tests"""
    print("\n" + "#" * 60)
    print("#" + " " * 58 + "#")
    print("#" + "  FILE INTEGRITY CHECKER - INSTALLATION TEST  ".center(58) + "#")
    print("#" + " " * 58 + "#")
    print("#" * 60)
    
    results = []
    
    # Run tests
    results.append(("Python Version", test_python_version()))
    results.append(("Required Modules", test_imports()))
    results.append(("Project Files", test_project_files()))
    results.append(("Hash Generation", test_hash_generation()))
    
    # Print summary
    print_header("Test Summary")
    
    all_passed = True
    for test_name, result in results:
        if result:
            print_status(test_name, "PASSED")
        else:
            print_status(test_name, "FAILED")
            all_passed = False
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("\n[SUCCESS] All tests passed!")
        print("\n[OK] Your installation is ready!")
        print("\nTo run the application:")
        print("   python app_gui.py")
        print("\nFor help, see:")
        print("   - README.md (overview)")
        print("   - USAGE_GUIDE.md (detailed instructions)")
        print("   - PROJECT_REPORT.md (technical details)")
    else:
        print("\n[WARNING] Some tests failed!")
        print("\nPlease fix the issues above before running the application.")
        print("\nCommon fixes:")
        print("   - Install Python 3.6+")
        print("   - Install Tkinter: pip install tk")
        print("   - Ensure all project files are present")
    
    print("\n" + "=" * 60 + "\n")
    
    return all_passed


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
