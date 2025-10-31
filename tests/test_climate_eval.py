import pytest
import numpy as np
from src.climate_eval import compute_grid_statistics

def test_grid_stats():
    data = np.array([[1.0, 2.0], [3.0, 4.0]])
    stats = compute_grid_statistics(data)
    assert stats["mean"] == 2.5
    assert stats["min"] == 1.0
    assert stats["max"] == 4.0
