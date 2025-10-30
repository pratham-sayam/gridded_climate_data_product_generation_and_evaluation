import numpy as np

def compute_grid_statistics(grid_data: np.ndarray):
    """Compute spatial statistics for climate grid matrix."""
    if grid_data.size == 0:
        return {"mean": 0.0, "std": 0.0, "min": 0.0, "max": 0.0}
    return {
        "mean": float(np.mean(grid_data)),
        "std": float(np.std(grid_data)),
        "min": float(np.min(grid_data)),
        "max": float(np.max(grid_data))
    }
