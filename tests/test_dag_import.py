from airflow.models import DagBag


def test_dag_import():
    dag_bag = DagBag(include_examples=False)
    assert len(dag_bag.import_errors) == 0
