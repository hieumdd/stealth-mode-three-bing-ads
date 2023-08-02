import pytest

from pipeline.pipeline import PIPELINES
from pipeline.accounts import ACCOUNTS
from pipeline.pipeline_service import run_pipeline

TIMEFRAME = [
    ("auto", (None, None)),
    ("manual", ("2023-01-01", "2023-08-01")),
]


@pytest.mark.parametrize(
    "_pipeline",
    PIPELINES.values(),
    ids=PIPELINES.keys(),
)
@pytest.mark.parametrize(
    "account",
    ACCOUNTS,
    ids=[i.id for i in ACCOUNTS],
)
@pytest.mark.parametrize(
    "timeframe",
    [i[1] for i in TIMEFRAME],
    ids=[i[0] for i in TIMEFRAME],
)
def test_pipeline_service(_pipeline, account, timeframe):
    res = run_pipeline(_pipeline, account, *timeframe)
    assert res
