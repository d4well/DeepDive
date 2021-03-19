
import pytest
from DeepDiveOOP_Project3 import Resource

@pytest.fixture
def resource_info():
    return {
        'name': 'Name',
        'manufacturer': 'AMD',
        'total': 10
    }

@pytest.fixture
def resource_i(resource):
    return Resource(**resource)

def test_instance_creation(resource_i):
    with pytest.raises(TypeError):
        Resource(**resource_i)

