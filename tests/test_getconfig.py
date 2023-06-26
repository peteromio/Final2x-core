import pytest

from src.utils.getConfig import SRCONFIG
from tests.util import load_image, CONFIG, calculate_image_similarity


class Test_SRCONFIG:
    def test_case_getConfigfromJson(self):
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[1], CONFIG()[3])

    def test_case_getConfigfromJson_Error(self):
        config = SRCONFIG()
        with pytest.raises(KeyError):
            config.getConfigfromJson(r'{"gpuid":0}', "sb114514")

    def test_case_getConfigfromYaml(self):
        config = SRCONFIG()
        config.getConfigfromYaml(CONFIG()[2], CONFIG()[3])

    def test_case_getConfigfromYaml_Error(self):
        config = SRCONFIG()
        with pytest.raises(FileNotFoundError):
            config.getConfigfromYaml("sb114514", "sb114514")

    def test_case_Settter_Error(self):
        config = SRCONFIG()
        with pytest.raises(TypeError):
            config.outputpath = 1
        with pytest.raises(TypeError):
            config.outputpath = '/114514-1919810-114514'
        with pytest.raises(TypeError):
            config.targetscale = 2
            config.targetscale = "1"
        with pytest.raises(TypeError):
            config.gpuid = "1"
        with pytest.raises(TypeError):
            config.tta = 114514
        with pytest.raises(TypeError):
            config.model = True
        with pytest.raises(TypeError):
            config.modelscale = "1"
        with pytest.raises(TypeError):
            config.modelnoise = "1"
        with pytest.raises(TypeError):
            config.inputpath = False
        with pytest.raises(ValueError):
            config.inputpath = []
