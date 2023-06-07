import pytest

from bing import pipeline, pipeline_service

TIMEFRAME = [
    ("auto", (None, None)),
    ("manual", ("2023-06-01", "2023-06-07")),
]


@pytest.mark.parametrize(
    "_pipeline",
    pipeline.pipelines.values(),
    ids=pipeline.pipelines.keys(),
)
@pytest.mark.parametrize(
    "account_id",
    ["176151959"],
)
@pytest.mark.parametrize(
    "timeframe",
    [i[1] for i in TIMEFRAME],
    ids=[i[0] for i in TIMEFRAME],
)
def test_pipeline_service(_pipeline, account_id, timeframe):
    res = pipeline_service.pipeline_service(_pipeline, account_id, *timeframe)
    assert res
