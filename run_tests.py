#!/usr/bin/env python3
"""
Main script to run Appium tests with different options
"""

import argparse
import subprocess
import sys
import os

def run_tests(platform=None, user_type=None, test_file=None, parallel=False, verbose=False):
    """
    Run tests with specified options
    
    Args:
        platform (str): Platform to test (android, ios, web)
        user_type (str): User type to test (user, advisor)
        test_file (str): Specific test file to run
        parallel (bool): Run tests in parallel
        verbose (bool): Verbose output
    """
    
    # Build pytest command
    cmd = ["pytest"]
    
    # Add platform marker
    if platform:
        cmd.extend(["-m", platform])
    
    # Add user type marker
    if user_type:
        cmd.extend(["-m", user_type])
    
    # Add specific test file
    if test_file:
        cmd.append(test_file)
    
    # Add parallel execution
    if parallel:
        cmd.extend(["-n", "auto"])
    
    # Add verbose output
    if verbose:
        cmd.append("-v")
    
    # Add HTML report
    cmd.extend(["--html=reports/report.html", "--self-contained-html"])
    
    print(f"Running command: {' '.join(cmd)}")
    print("Using: LambdaTest Hub")
    
    try:
        # Run tests
        result = subprocess.run(cmd, check=True)
        print("Tests completed successfully!")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Tests failed with exit code: {e.returncode}")
        return e.returncode
    except KeyboardInterrupt:
        print("\nTests interrupted by user")
        return 1

def main():
    """Main function to parse arguments and run tests"""
    
    parser = argparse.ArgumentParser(description="Run Appium tests with different options")
    
    parser.add_argument(
        "--platform", 
        choices=["android", "ios", "web"],
        help="Platform to test (android, ios, web)"
    )
    
    parser.add_argument(
        "--user-type",
        choices=["user", "advisor"],
        help="User type to test (user, advisor)"
    )
    
    parser.add_argument(
        "--test-file",
        help="Specific test file to run"
    )
    
    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Run tests in parallel"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    parser.add_argument(
        "--list-tests",
        action="store_true",
        help="List available tests without running them"
    )
    

    
    args = parser.parse_args()
    
    if args.list_tests:
        # List available tests
        print("Available test files:")
        test_files = []
        for root, dirs, files in os.walk("tests"):
            for file in files:
                if file.startswith("test_") and file.endswith(".py"):
                    test_files.append(os.path.join(root, file))
        
        for test_file in sorted(test_files):
            print(f"  {test_file}")
        return 0
    
    # Run tests
    return run_tests(
        platform=args.platform,
        user_type=args.user_type,
        test_file=args.test_file,
        parallel=args.parallel,
        verbose=args.verbose
    )

if __name__ == "__main__":
    sys.exit(main())
    
