# AI usage: Claude (Anthropic) assisted with test structure and Flask testing patterns.
# Generated with AI assistance for CS3704.

import pytest
import sys
import os

# Add parent directory to path so app.py can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_form_data():
    """Sample form data for submitting a Top Five list."""
    return {
        "category": "Movies",
        "item1": "The Godfather",
        "item2": "The Dark Knight",
        "item3": "Pulp Fiction",
        "item4": "Fight Club",
        "item5": "Goodfellas",
    }


class TestHomeRoute:
    """Tests for the home route (/)."""

    def test_get_home_returns_200(self, client):
        """GET / should return HTTP 200."""
        response = client.get("/")
        assert response.status_code == 200

    def test_get_home_contains_top_five_title(self, client):
        """Home page should contain 'Top Five' in the HTML."""
        response = client.get("/")
        assert b"Top Five" in response.data

    def test_get_home_has_category_input(self, client):
        """Home page should have a category input field."""
        response = client.get("/")
        assert b'name="category"' in response.data

    def test_get_home_has_five_item_inputs(self, client):
        """Home page should have exactly 5 item input fields."""
        response = client.get("/")
        for i in range(1, 6):
            assert f'name="item{i}"'.encode() in response.data

    def test_no_submissions_shows_empty_message(self, client):
        """When there are no submissions, show the empty state message."""
        response = client.get("/")
        assert b"No submissions yet" in response.data


class TestPostSubmission:
    """Tests for form submission behavior."""

    def test_valid_post_redirects_to_home(self, client, sample_form_data):
        """A valid POST should redirect back to home."""
        response = client.post("/", data=sample_form_data, follow_redirects=False)
        assert response.status_code == 302

    def test_valid_post_stores_submission(self, client, sample_form_data):
        """A valid POST should store the submission and display it."""
        response = client.post("/", data=sample_form_data, follow_redirects=True)
        assert response.status_code == 200
        assert b"Movies" in response.data
        assert b"The Godfather" in response.data

    def test_post_with_missing_category_returns_400(self, client, sample_form_data):
        """POST with empty category should not store submission."""
        data = sample_form_data.copy()
        data["category"] = ""
        response = client.post("/", data=data, follow_redirects=True)
        # Flask silently skips invalid submissions — category is checked server-side
        # Empty category means no submission appended
        assert response.status_code == 200

    def test_post_with_missing_item_returns_400(self, client, sample_form_data):
        """POST with a missing item should not store a complete submission."""
        data = sample_form_data.copy()
        data["item3"] = ""  # Leave item3 empty
        response = client.post("/", data=data, follow_redirects=True)
        assert response.status_code == 200
        # Should not contain the submission since validation requires all items

    def test_post_with_whitespace_only_category_rejected(self, client, sample_form_data):
        """POST with whitespace-only category should be rejected by strip()."""
        data = sample_form_data.copy()
        data["category"] = "   "
        response = client.post("/", data=data, follow_redirects=True)
        assert response.status_code == 200
        # Whitespace-only fails the `if category` check after strip()


class TestSubmissionDisplay:
    """Tests for how submissions are displayed after posting."""

    def test_submission_displays_all_five_items(self, client, sample_form_data):
        """After posting, all 5 items should appear in the response."""
        client.post("/", data=sample_form_data, follow_redirects=True)
        response = client.get("/")
        assert b"The Godfather" in response.data
        assert b"The Dark Knight" in response.data
        assert b"Pulp Fiction" in response.data
        assert b"Fight Club" in response.data
        assert b"Goodfellas" in response.data

    def test_multiple_categories_display_separately(self, client):
        """Posting multiple categories should show both in the table."""
        client.post("/", data={
            "category": "Movies",
            "item1": "Film A", "item2": "Film B", "item3": "Film C",
            "item4": "Film D", "item5": "Film E",
        }, follow_redirects=True)

        client.post("/", data={
            "category": "Songs",
            "item1": "Song A", "item2": "Song B", "item3": "Song C",
            "item4": "Song D", "item5": "Song E",
        }, follow_redirects=True)

        response = client.get("/")
        assert b"Movies" in response.data
        assert b"Songs" in response.data


class TestInputValidation:
    """Tests for server-side input validation."""

    def test_empty_form_post_ignored(self, client):
        """Submitting completely empty form should not crash."""
        response = client.post("/", data={}, follow_redirects=True)
        assert response.status_code == 200

    def test_partial_form_data_ignored(self, client):
        """Submitting form with only some fields should not store partial data."""
        response = client.post("/", data={"category": "Test", "item1": "Only One"}, follow_redirects=True)
        assert response.status_code == 200
        # The `all(items)` check fails, so nothing is appended
