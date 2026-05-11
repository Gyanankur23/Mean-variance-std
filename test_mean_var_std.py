import unittest
import numpy as np
from mean_var_std import calculate


class MeanVarStdTests(unittest.TestCase):
    """Unit tests for mean-variance-standard deviation calculator."""
    
    def test_calculate_output(self):
        """Test that calculate returns correct structure."""
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        
        # Check keys exist
        expected_keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
        for key in expected_keys:
            self.assertIn(key, result)
        
        # Check structure - each key should have 3 items (axis0, axis1, flattened)
        for key in expected_keys:
            self.assertEqual(len(result[key]), 3)
    
    def test_calculate_values(self):
        """Test that calculate returns correct values."""
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        
        # Expected matrix:
        # [[0, 1, 2],
        #  [3, 4, 5],
        #  [6, 7, 8]]
        
        # Mean along axis 0 (columns): [3, 4, 5]
        self.assertEqual(result['mean'][0], [3.0, 4.0, 5.0])
        
        # Mean along axis 1 (rows): [1, 4, 7]
        self.assertEqual(result['mean'][1], [1.0, 4.0, 7.0])
        
        # Mean of flattened: 4.0
        self.assertEqual(result['mean'][2], 4.0)
        
        # Sum of flattened: 36
        self.assertEqual(result['sum'][2], 36.0)
    
    def test_invalid_input(self):
        """Test that calculate raises error for invalid input length."""
        with self.assertRaises(ValueError) as context:
            calculate([1, 2, 3])
        
        self.assertEqual(str(context.exception), "List must contain nine numbers.")
    
    def test_variance_values(self):
        """Test variance calculations."""
        result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
        
        # Manual calculation check
        matrix = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
        
        # Variance along axis 0
        expected_var_axis0 = matrix.var(axis=0).tolist()
        self.assertEqual(result['variance'][0], expected_var_axis0)
        
        # Variance along axis 1
        expected_var_axis1 = matrix.var(axis=1).tolist()
        self.assertEqual(result['variance'][1], expected_var_axis1)
    
    def test_std_deviation(self):
        """Test standard deviation calculations."""
        result = calculate([2, 4, 6, 8, 10, 12, 14, 16, 18])
        
        # std should be sqrt of variance
        var_flat = result['variance'][2]
        std_flat = result['standard deviation'][2]
        self.assertAlmostEqual(std_flat, np.sqrt(var_flat))


if __name__ == "__main__":
    unittest.main()
