from awmt.proto_dsp_tools import example

def test_add_one():
    x = example.add_one(0)
    assert x == 1