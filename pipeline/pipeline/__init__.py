from pipeline.pipeline import campaign_performance_report

PIPELINES = {i.name: i for i in [campaign_performance_report.pipeline]}
