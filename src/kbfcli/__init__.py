"""KanbanFlow client"""


def run_kbf_client(args):
    """Run the KanbanFlow client"""
    from .run import run
    return run(args)


__all__ = ["run_kbf_client"]
