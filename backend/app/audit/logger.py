import json
from datetime import datetime
from typing import Dict, Any


def log_event(
    action: str,
    actor: str,
    resource: str,
    metadata: Dict[str, Any] | None = None,
):
    """
    Records an auditable system event.

    Args:
        action: What happened (e.g. 'document_uploaded')
        actor: Who performed the action (user, system, reviewer)
        resource: What the action was performed on
        metadata: Extra contextual information
    """
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "actor": actor,
        "action": action,
        "resource": resource,
        "metadata": metadata or {},
    }

    with open("audit.log", "a") as log_file:
        log_file.write(json.dumps(event) + "\n")