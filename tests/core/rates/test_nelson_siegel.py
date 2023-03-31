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

import approvaltests as at
import numpy as np
import pandas as pd
import pytest

import aenc as ae


def test_zero_rates() -> None:
    """Test creating zero rates from betas."""

    # Create Nelson-Siegel object
    obj = ae.NelsonSiegel()
    obj.lambda_ = 0.7308  # Recommended in Diebold and Li (2006)
    obj.maturities = np.array([0.25, 1.0])

    # Create DF with betas
    row_count = 3
    row_index = [f'sample{row_index}' for row_index in range(row_count)]
    beta_1 = np.linspace(0.0, 1.0, row_count)
    beta_2 = np.linspace(0.5, 1.5, row_count)
    beta_3 = np.linspace(1.0, 2.0, row_count)
    beta_df = pd.DataFrame({"beta_1": beta_1, "beta_2": beta_2, "beta_3": beta_3}, index=row_index)

    # Verify zero rates
    zero_rates_df = obj.get_zero_rates(beta_df)
    at.verify(zero_rates_df)


if __name__ == "__main__":
    pytest.main([__file__])
