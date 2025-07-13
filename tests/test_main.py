import unittest
from unittest.mock import patch, MagicMock
import os

# Set a dummy API key for testing
os.environ["OPENAI_API_KEY"] = "test_api_key"

from main import (
    generate_business_idea,
    client_engagement_conversation,
    build_personal_brand,
)

class TestMain(unittest.TestCase):
    @patch("main.llm")
    def test_generate_business_idea(self, mock_llm):
        # Configure the mock to behave like the real object
        mock_llm.return_value = "Test business idea"

        # Call the function
        result = generate_business_idea()

        # Assert the result
        self.assertEqual(result, "Test business idea")

    @patch("main.llm")
    def test_client_engagement_conversation(self, mock_llm):
        # Configure the mock
        mock_llm.return_value = "Test conversation starter"

        # Call the function
        result = client_engagement_conversation()

        # Assert the result
        self.assertEqual(result, "Test conversation starter")

    @patch("main.llm")
    def test_build_personal_brand(self, mock_llm):
        # Configure the mock
        mock_llm.return_value = "Test branding tips"

        # Call the function
        result = build_personal_brand()

        # Assert the result
        self.assertEqual(result, "Test branding tips")

if __name__ == "__main__":
    unittest.main()
