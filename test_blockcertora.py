# test_blockcertora.py
"""
Tests for BlockCertora module.
"""

import unittest
from blockcertora import BlockCertora

class TestBlockCertora(unittest.TestCase):
    """Test cases for BlockCertora class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockCertora()
        self.assertIsInstance(instance, BlockCertora)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockCertora()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
