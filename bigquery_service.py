from datetime import datetime

from google.cloud import bigquery

DATASET = "BingAds"

client = bigquery.Client()

def load(table: str, schema: list[dict]):
    def _load(rows: list[dict]) -> int:
        if not rows:
            return 0

        return (
            client.load_table_from_json( # type: ignore
                [
                    {
                        **row,
                        "_batched_at": datetime.utcnow().isoformat(timespec="seconds"),
                    }
                    for row in rows
                ],
                f"{DATASET}.{table}",
                job_config=bigquery.LoadJobConfig(
                    schema=[*schema, {"name": "_batched_at", "type": "TIMESTAMP"}],
                    create_disposition="CREATE_IF_NEEDED",
                    write_disposition="WRITE_APPEND",
                ),
            )
            .result()
            .output_rows
        )

    return _load
