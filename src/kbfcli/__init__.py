"""KanbanFlow client"""


def run_kbf_client():
    """Run the KanbanFlow client"""
    from .run import run
    run()


__all__ = ["run_kbf_client"]
