from .._base import IDNeighborsClassifier
from ._cca_transformer import CCATransformer


class GNN(IDNeighborsClassifier):
    """Normalized KNN"""
    def fit(self, X, y, spp=None):
        X = CCATransformer().fit_transform(X, spp=spp)
        return super().fit(X, y)
    
    def predict(self, X, spp=None):
        X = CCATransformer().fit_transform(X, spp=spp)
        return super().predict(X)