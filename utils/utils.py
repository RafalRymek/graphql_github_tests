import json
from pathlib import Path


def get_env() -> dict:
    """
    Returns url and login parameters of chosen environment
    :param env: which environment parameters should be returned
    """

    config_file = str(Path(Path(__file__).parent.parent, "config.json"))

    try:
        with open(config_file) as json_file:
            return json.load(json_file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Incorrect config.json file. {error.msg} on line #{error.lineno}. "
            f"Please fix your config.json file and try ones again"
        )
    except KeyError:
        raise KeyError(f"Unexpected env '{env.upper()}'." f"Check your behave.ini file for available variables")
