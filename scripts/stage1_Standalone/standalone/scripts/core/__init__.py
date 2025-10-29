# -*- coding: utf-8 -*-
"""
HVDC Pipeline Core Module (Standalone Package)
==============================================

Central header matching and detection system for all pipeline stages.
Standalone package includes only essential modules for Stage 1 synchronization.
"""

from .header_normalizer import HeaderNormalizer, normalize_header
from .semantic_matcher import SemanticMatcher, find_header_by_meaning
from .header_registry import HeaderRegistry, HVDC_HEADER_REGISTRY, HeaderCategory, HeaderDefinition
from .standard_header_order import (
    STANDARD_HEADER_ORDER,
    STAGE2_HEADER_ORDER,
    STAGE1_BASE_COLS_ORDER,
    HeaderOrderManager,
    reorder_dataframe_columns,
)

# Minimal detect_header_row implementation (header_detector not included in standalone)
def detect_header_row(xlsx_path: str, sheet_name: str, max_scan_rows: int = 20):
    """
    Minimal header row detection for standalone package.
    Returns row index and confidence score.

    Args:
        xlsx_path: Path to Excel file
        sheet_name: Name of the sheet
        max_scan_rows: Maximum rows to scan

    Returns:
        Tuple of (row_index, confidence)
    """
    try:
        import pandas as pd

        xl = pd.ExcelFile(xlsx_path, engine="openpyxl")
        df = pd.read_excel(xl, sheet_name=sheet_name, header=None, nrows=max_scan_rows)

        # Simple heuristic: find first row with mostly text and many non-null values
        best_idx = 0
        best_score = 0.0

        for idx in range(min(max_scan_rows, len(df))):
            row = df.iloc[idx]
            non_null = row.notna().sum()
            if non_null == 0:
                continue
            text_count = sum(1 for v in row if isinstance(v, str) and str(v).strip())
            score = (non_null / len(row)) * 0.5 + (text_count / non_null) * 0.5

            if score > best_score:
                best_score = score
                best_idx = idx
    except Exception:
        # Fallback: assume header is at row 0
        best_idx = 0
        best_score = 0.7

    confidence = max(0.0, min(1.0, best_score))
    return best_idx, confidence

# Convenience functions for getting warehouse/site/date columns from registry
def get_warehouse_columns(use_primary_alias=True):
    """Get warehouse columns from central registry."""
    return HVDC_HEADER_REGISTRY.get_warehouse_columns(use_primary_alias)

def get_site_columns(use_primary_alias=True):
    """Get site columns from central registry."""
    return HVDC_HEADER_REGISTRY.get_site_columns(use_primary_alias)

def get_date_columns(use_primary_alias=True):
    """Get date columns from central registry."""
    return HVDC_HEADER_REGISTRY.get_date_columns(use_primary_alias)

__version__ = "1.2.0-standalone"
__all__ = [
    "HeaderNormalizer",
    "normalize_header",
    "SemanticMatcher",
    "find_header_by_meaning",
    "HeaderRegistry",
    "HVDC_HEADER_REGISTRY",
    "HeaderCategory",
    "HeaderDefinition",
    "STANDARD_HEADER_ORDER",
    "STAGE2_HEADER_ORDER",
    "STAGE1_BASE_COLS_ORDER",
    "HeaderOrderManager",
    "reorder_dataframe_columns",
    "get_warehouse_columns",
    "get_site_columns",
    "get_date_columns",
    "detect_header_row",
]
