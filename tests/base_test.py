import pytest
from all_relative import parsers


class BaseTest:
    _classname: str
    _ext: str

    _input_template: str
    _output_template: str

    input_str: str
    output_str: str

    @pytest.fixture(autouse=True)
    def _render(self, jinja_env):
        input_str = jinja_env.from_string(self._input_template).render()
        output_str = jinja_env.from_string(self._output_template).render()

        self.input_str = input_str
        self.output_str = output_str

    def test_ext_parser(self):
        Parser = getattr(parsers, self._classname)
        parser = Parser()

        assert parser.parse_string(self.input_str) == self.output_str

    def test_parser(self):
        parser = parsers.Parser()

        assert parser.parse_string(self.input_str, ext=self._ext) == self.output_str
