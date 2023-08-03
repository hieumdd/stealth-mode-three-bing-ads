from pipeline.accounts import ACCOUNTS
from pipeline.pipeline.campaign_performance_report import (
    pipeline as CampaignPerformanceReport,
)
from pipeline.pipeline_service import run_pipeline


def main(request):
    data = request.get_json(silent=True)
    print(data)

    response = {
        "result": [
            run_pipeline(
                CampaignPerformanceReport,
                account,
                data.get("start"),
                data.get("end"),
            )
            for account in ACCOUNTS
        ]
    }

    print(response)
    return response
