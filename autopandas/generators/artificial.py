# Artificial data generator

#from ..autopandas import from_X_y
import autopandas
from sklearn.datasets import make_moons
from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_circles

class Artificial():
    """ Artificial data generator.
        Generate 2D classification datasets.
    """
    def __init__(self, method='moons', n=100):
        """ Initalize the artificial data generator.
        
            :param method: 'moons', 'blobs' or 'circles'.
        """
        if method == 'moons':
            X, y = make_moons(n_samples=n, noise=0.1)
        elif method == 'blobs':
            X, y = make_blobs(n_samples=n, centers=3, n_features=2)
        elif method == 'circles':
            X, y = make_circles(n_samples=n, noise=0.05)
        else:
            raise Exception('Unknown method: {}'.format(method))
        # Create AutoData frame from X and y
        self.data = autopandas.from_X_y(X, y)

    def sample(self, n=1, replace=True):
        if self.data is None:
            raise Exception('You firstly need to train the Copycat before sampling. Please use fit method.')
        else:
            return self.data.sample(n, replace=replace)