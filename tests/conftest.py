import pytest
import jinja2


@pytest.fixture(scope="module")
def jinja_env():
    loader = jinja2.PackageLoader("tests")
    env = jinja2.Environment(
        loader=loader,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    return env
