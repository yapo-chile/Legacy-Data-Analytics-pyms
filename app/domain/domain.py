from typing import Any, Dict, NewType

# Json format
JSONType = NewType("JSONType", Dict[str, Any])

# Api Rest Code Status format
StatusCode = NewType("StatusCode", int)
