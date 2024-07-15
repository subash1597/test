# tests/unit/tables/test_string_matching.py

import pytest

class TestStringMatching:

    @pytest.fixture
    def sample_data(self):
        return {
            "correct_prefix": "DI_TABLE",
            "incorrect_prefix": "TABLE_DI",
            "required_tables": ["DI_DASHBOARD", "DI_WIDGET", "DI_INSIGHT", "DI_FEEDBACK"],
            "all_tables": ["DI_DASHBOARD", "DI_WIDGET", "DI_INSIGHT", "DI_FEEDBACK", "OTHER_TABLE"]
        }

    def test_string_startswith_di(self, sample_data):
        assert sample_data["correct_prefix"].startswith("DS")
        assert not sample_data["incorrect_prefix"].startswith("DI")

    def test_required_tables_present(self, sample_data):
        for table in sample_data["required_tables"]:
            assert table in sample_data["all_tables"]
