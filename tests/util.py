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
