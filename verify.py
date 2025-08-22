import sys
import subprocess

def run_verifier(filename):
    """Runs the Mizar verifier on a given file."""
    if not filename:
        print("Error: Please provide a filename.")
        print("Usage: python verify.py <your_proof.miz>")
        return

    print(f"Verifying {filename}...")
    try:
        result = subprocess.run(
            ['mizf', filename],
            capture_output=True,
            text=True
        )
        # Print the combined output
        print(result.stdout + result.stderr)
    except FileNotFoundError:
        print("Error: 'mizf' command not found. Are you running this inside the Mizar Dev Container?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Get filename from command line arguments
    file_to_check = sys.argv[1] if len(sys.argv) > 1 else None
    run_verifier(file_to_check)
