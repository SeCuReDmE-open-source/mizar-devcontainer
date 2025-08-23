import pytest
from unittest.mock import patch
from verify import run_verifier

def test_run_verifier_no_filename(capsys):
    """
    Test that run_verifier prints an error message when no filename is provided.
    """
    run_verifier(None)
    captured = capsys.readouterr()
    assert "Error: Please provide a filename." in captured.out
    assert "Usage: python verify.py <your_proof.miz>" in captured.out

@patch('verify.subprocess.run')
def test_run_verifier_with_filename(mock_subprocess_run):
    """
    Test that run_verifier calls subprocess.run with the correct arguments.
    """
    filename = "tests/test.miz"
    run_verifier(filename)
    mock_subprocess_run.assert_called_once_with(
        ['mizf', filename],
        capture_output=True,
        text=True
    )

@patch('verify.subprocess.run')
def test_run_verifier_file_not_found(mock_subprocess_run, capsys):
    """
    Test that run_verifier handles FileNotFoundError correctly.
    """
    mock_subprocess_run.side_effect = FileNotFoundError
    filename = "tests/test.miz"
    run_verifier(filename)
    captured = capsys.readouterr()
    assert "Error: 'mizf' command not found." in captured.out

@patch('verify.subprocess.run')
def test_run_verifier_unexpected_error(mock_subprocess_run, capsys):
    """
    Test that run_verifier handles other exceptions correctly.
    """
    mock_subprocess_run.side_effect = Exception("Something went wrong")
    filename = "tests/test.miz"
    run_verifier(filename)
    captured = capsys.readouterr()
    assert "An unexpected error occurred: Something went wrong" in captured.out
