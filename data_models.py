from typing import TypedDict

class CustomerSegment(TypedDict):
    segment_id: str
    demographics: Dict[str, str]
    behavior_patterns: Dict[str, float]

class ExperimentResult(TypedDict):
    experiment_id: str
    metrics: Dict[str, float]
    conclusions: Dict[str, str]