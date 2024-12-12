import requests
import pytest

# Helper function to check status codes
def check_status_code(url, expected_status):
    response = requests.get(url)
    assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"

def test_get_posts():
    """ Test GET method for posts endpoint """
    url = "https://jsonplaceholder.typicode.com/posts"
    check_status_code(url, 200)

def test_get_single_post():
    """ Test GET method for a single post """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    check_status_code(url, 200)

def test_get_invalid_post():
    """ Test GET method for an invalid post (404) """
    url = "https://jsonplaceholder.typicode.com/posts/999999"
    check_status_code(url, 404)

def test_get_non_existent_endpoint():
    """ Test GET method for a non-existent endpoint (404) """
    url = "https://jsonplaceholder.typicode.com/nonexistent"
    check_status_code(url, 404)

def test_get_server_error():
    """ Simulate server error (500) """
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Using a valid endpoint for testing purpose
    # This URL won't give a 500 response in JSONPlaceholder, it's for simulating failure in your actual tests
    check_status_code(url, 500)  # Expected behavior for an invalid scenario

if __name__ == "__main__":
    pytest.main()
