import numpy as np
from sklearn.base import (
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
)

from . import StandardScalerWithDOF
from ._ccora import CCorA


class CCorATransformer(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):
    @property
    def _n_features_out(self):
        return self.ccora_.projector.shape[1]

    def get_feature_names_out(self, input_features=None) -> np.ndarray:
        return np.asarray(
            [f"ccora{i}" for i in range(self._n_features_out)], dtype=object
        )

    def fit(self, X, y):
        X = self._validate_data(X, reset=True)

        self.scaler_ = StandardScalerWithDOF(ddof=1).fit(X)
        y = StandardScalerWithDOF(ddof=1).fit_transform(y)
        self.ccora_ = CCorA(self.scaler_.transform(X), y)
        return self

    def transform(self, X, y=None):
        return self.scaler_.transform(X) @ self.ccora_.projector

    def fit_transform(self, X, y):
        return self.fit(X, y).transform(X)
