from snowflake.cell import hex_state


def make_state(arr, default):
    """
    Convert from:
    [
        [a, b, c, d, e,],
        [f, g, h, i, j,],
        [k, l, m, n, o,],
    ]
    To:
         a
            b
         f     c
            g     d
         k     h     e
            l     i
               m     j
                  n
                     o
    """
    return hex_state(
            (((x, y), val)
             for (x, row) in enumerate(arr)
             for (y, val) in enumerate(row)),
            default=default)


def test_initial_state_empty():
    s = hex_state()
    assert len(s) == 0


def test_default():
    s = hex_state(default=1)
    assert s[0,0] == 1


def test_neighboring_items():
    s = make_state([
            [1, 2, 3,],
            [4, 5, 6,],
            [7, 8, 9,],
        ],
        default=0)
    #        1
    #           2
    #        4     3
    #           5
    #        7     6
    #           8
    #              9
    assert s[1, 1] == 5
    assert sum(s.neighboring_values(1, 1)) == sum([2, 3, 6, 8, 7, 4])


def test_default_neighbors():
    s = make_state([
            [1, 2, 3,],
            [4, 5, 6,],
        ],
        default=-1)
    #        1
    #           2
    #        4     3
    #           5
    #              6
    assert s[0, 1] == 2
    assert sum(s.neighboring_values(0, 1)) == sum([-1, -1, 3, 5, 4, 1])


def test_map():
    s1 = make_state([
            [1, 2, 3,],
            [4, 5, 6,],
        ], default=-1)
    #        1
    #           2
    #        4     3
    #           5
    #              6
    s2 = s1.map(lambda v: v+5)
    assert s2[0, 1] == 7
    assert sum(s2.neighboring_values(0, 1)) == sum([-1, -1, 8, 10, 9, 6])


def test_map_with_neighbors():
    s1 = make_state([
            [1, 2, 3,],
            [4, 5, 6,],
        ], default=-1)
    #        1
    #           2
    #        4     3
    #           5
    #              6
    s2 = s1.map_with_neighbors(lambda v, neighbors: sum([v, *neighbors]))
    assert s2[0, 1] == sum([2, -1, -1, 3, 5, 4, 1])
