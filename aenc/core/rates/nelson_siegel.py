# Copyright (C) 2023-present The Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class NelsonSiegel:
    """Nelson-Siegel curve basis."""

    maturities: np.ndarray = field(default=None)
    """Maturities in years for which zero rates are defined."""

    lambda_: float = field(default=None)
    """Nelson-Siegel parameter lambda."""

    def get_zero_rates(self, betas: pd.DataFrame) -> pd.DataFrame:
        """Converts dataframe of Nelson-Siegel parameters beta_1,2,3 to dataframe of zero rates."""

        # Check that all maturities are positive with 1e-10 tolerance (zero maturities are not allowed)
        if not all(self.maturities >= 1e-10):
            raise RuntimeError("Only positive maturities are accepted by NelsonSiegel.get_zero_rates method.")

        # Basis loadings
        count = len(self.maturities)
        lm = self.lambda_ * self.maturities
        e = np.exp(-lm)
        loading_1 = np.ones(count)
        loading_2 = (1.0 - e) / lm
        loading_3 = loading_2 - e

        # Basis weights
        row_index = betas.index
        beta_1 = betas["beta_1"].values
        beta_2 = betas["beta_2"].values
        beta_3 = betas["beta_3"].values

        # Calculate zero rates
        prod_1 = np.outer(beta_1, loading_1)
        prod_2 = np.outer(beta_2, loading_2)
        prod_3 = np.outer(beta_3, loading_3)
        zero_rate_arr = prod_1 + prod_2 + prod_3

        result = pd.DataFrame(data=zero_rate_arr, index=row_index, columns=self.maturities)
        return result
