from typing import Optional
from datetime import datetime, date, timedelta

from compose import compose

import bigquery_service
import bing_service
from pipeline.pipeline.interface import Pipeline
from pipeline.accounts import Account

DATE_FORMAT = "%Y-%m-%d"


def run_pipeline(
    pipeline: Pipeline,
    account: Account,
    start: Optional[str],
    end: Optional[str],
):
    auth_data = bing_service.get_auth_data(account.refresh_token())

    _end = datetime.strptime(end, DATE_FORMAT).date() if end else date.today()
    _start = (
        datetime.strptime(start, DATE_FORMAT).date()
        if start
        else date.today() - timedelta(days=30)
    )

    reporting_service = bing_service.get_reporting_service(auth_data)

    return compose(
        lambda x: {"output_rows": x},
        bigquery_service.load(f"p_{pipeline.name}__{account.id}", pipeline.schema),
        pipeline.transform_fn,
        lambda report: [i for i in report.report_records],
        bing_service.get_report(auth_data),
        pipeline.build_fn(reporting_service),
    )(account.id, (_start, _end))
