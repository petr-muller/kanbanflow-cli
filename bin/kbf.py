"""Main executable for the KanbanFlow client"""

import sys

if __name__ == "__main__":
    import kbfcli
    raise SystemExit(kbfcli.run_kbf_client(sys.argv[1:]))
