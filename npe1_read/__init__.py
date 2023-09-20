import numpy as np
from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_get_reader(path: str):
    if not path.endswith(".npy"):
        return None
    return reader_function


def reader_function(path: str):
    data = np.load(path)
    return [(data, {}, 'image')]
