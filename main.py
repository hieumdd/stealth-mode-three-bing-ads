from pipeline.pipeline.campaign_performance_report import (
    pipeline as CampaignPerformanceReport,
)
from pipeline.pipeline_service import run_pipeline


def main(request):
    data = request.get_json(silent=True)
    print(data)

    response = run_pipeline(
        CampaignPerformanceReport,
        "176151959",
        data.get("start"),
        data.get("end"),
    )

    print(response)
    return response
