import pytest
import re
from snowflake.snowpark import Session

class TestConnection:
    
    @pytest.fixture
    def get_connection_params(self):
        connection_parameters = {
            "ACCOUNT": "RSS-PRIMARY",
            "USER": "sbmathiyalagan@ucdavis.edu",
            "AUTHENTICATOR": "externalbrowser",
            "ROLE": "RSS-US-TEAM-PRAGYA-OFFSHORE",
            "WAREHOUSE": "ML_XSMALL",
            "DATABASE": "RSS_DEV",
            "SCHEMA": "ML"
        }
        return connection_parameters
    
    def test_connection_params_structure(self, get_connection_params):
        # Test to ensure the connection parameters have the required keys
        required_keys = ["ACCOUNT", "USER", "AUTHENTICATOR", "ROLE", "WAREHOUSE", "DATABASE", "SCHEMA"]
        for key in required_keys:
            assert key in get_connection_params

    def test_valid_params(self, get_connection_params):
        # Test to ensure the connection parameters have valid values
        assert get_connection_params['SCHEMA'] == 'ML', "Schema should be 'ML'"
        assert get_connection_params['DATABASE'] == 'RSS_DEV', "Database should be 'RSS_DEV'"
        # Add more assertions as needed for other parameters


    def test_connection_format(self, get_connection_params):
        # Test to ensure the parameters have the expected format

        # account
        assert isinstance(get_connection_params['ACCOUNT'], str), "Account should be a string"
        assert get_connection_params['ACCOUNT'].isupper(), "Account should be in uppercase"

        # email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        assert re.match(email_regex, get_connection_params['USER']), "User should be a valid email address"

        # role
        assert isinstance(get_connection_params['ROLE'], str), "Role should be a string"
        assert get_connection_params['ROLE'], "Role should not be empty"

        # warehouse
        assert isinstance(get_connection_params['WAREHOUSE'], str), "Warehouse should be a string"
        assert get_connection_params['WAREHOUSE'], "Warehouse should not be empty"

        # authenticator
        expected_authenticator = "externalbrowser"
        assert get_connection_params['AUTHENTICATOR'] == expected_authenticator, f"Authenticator should be '{expected_authenticator}'"
