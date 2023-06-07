from bing.pipeline.campaign_performance_report import (
    pipeline as CampaignPerformanceReport,
)
from bing.pipeline_service import pipeline_service


def main(request):
    data = request.get_json(silent=True)
    print(data)

    response = pipeline_service(
        CampaignPerformanceReport,
        "176151959",
        data.get("start"),
        data.get("end"),
    )

    print(response)
    return response
