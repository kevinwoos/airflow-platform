def on_failure_callback(context):
    dag_id = context["dag"].dag_id
    task_id = context["task_instance"].task_id
    exc = context.get("exception")
    print(f"[FAILURE] dag_id={dag_id}, task_id={task_id}, exception={exc}")
