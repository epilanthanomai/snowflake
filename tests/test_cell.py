from snowflake.cell import cell

def test_default_cell_empty():
    c = cell()
    assert len(c) == 0
