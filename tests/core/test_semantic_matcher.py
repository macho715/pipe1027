import io
import sys
import types
from contextlib import redirect_stdout
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

if "pandas" not in sys.modules:
    pandas_stub = types.ModuleType("pandas")
    pandas_stub.DataFrame = type("DataFrame", (), {})  # type: ignore[attr-defined]
    pandas_stub.Series = type("Series", (), {})  # type: ignore[attr-defined]
    sys.modules["pandas"] = pandas_stub
if "numpy" not in sys.modules:
    numpy_stub = types.ModuleType("numpy")
    sys.modules["numpy"] = numpy_stub

from scripts.core.semantic_matcher import MatchReport, MatchResult  # type: ignore[attr-defined]


def test_print_summary_formats_column_name_without_literal_format_spec():
    report = MatchReport(
        total_semantic_keys=1,
        successful_matches=1,
        failed_matches=0,
        average_confidence=0.95,
        results=[
            MatchResult(
                semantic_key="case_number",
                matched=True,
                column_name="Case No.",
                confidence=0.92,
                match_type="exact",
            )
        ],
    )

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        report.print_summary()

    summary = buffer.getvalue()
    assert ":<30s" not in summary
    assert "'Case No." in summary
