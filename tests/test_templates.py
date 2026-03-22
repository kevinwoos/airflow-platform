from dags.templates.sftp_template import create_sftp_dag


def test_create_sftp_dag():
    dag = create_sftp_dag(
        dag_id="test_sftp",
        schedule="0 1 * * *",
        source_path="/from",
        target_path="/to",
        tags=["test"],
    )
    assert dag.dag_id == "test_sftp"
    assert "test" in dag.tags
