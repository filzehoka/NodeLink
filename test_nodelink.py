# test_nodelink.py
"""
Tests for NodeLink module.
"""

import unittest
from nodelink import NodeLink

class TestNodeLink(unittest.TestCase):
    """Test cases for NodeLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeLink()
        self.assertIsInstance(instance, NodeLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
