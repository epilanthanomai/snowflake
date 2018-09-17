from snowflake.reiter import transition
from util import make_state


def assert_state_equal(expect, actual):
    # Floating point math makes everything harder.
    #
    # We want to verify that each value in expect is also in actual, to
    # within threshold difference. When that fails, we also want an error
    # message that clearly shows what values were wrong, especially if we
    # manually run pytest -vv. We get our best error messages from pytest if
    # we assert ==, but of course comparing expect exactly to actual will
    # flag differences in our floating-point threshold, which isn't very
    # helpful.
    #
    # So our strategy here is to fudge over differences if they're within
    # the threshold. We'll construct list-based versions of our expect and
    # actual values for display for prettier error messages. Then we'll
    # construct a fudged version of our actual values, such that if an
    # actual value is within the threshold it'll be replaced with the
    # expected value. That way when we compare this fudged version against
    # the expected values, the values within the threshold show exactly
    # equal to the expected value. Hopefully they all will. But when
    # something inevitably fails, the out-of-threshold actual values will
    # remain in the fudged list and will be clearly visible as errors in the
    # assert.
    #
    # To get there, we filter out the expected values that we care about,
    # then we calculate parallel actual and difference lists based on those.
    # We zip them together, and then we reconstruct our fidged value for
    # testing.

    threshold = 0.001

    expect_list = list(sorted(
        ((x, y), v) for ((x, y), v) in expect.items()))
    actual_list = [
        actual[x, y] for ((x, y), _) in expect_list]
    difference_list = [
        e - actual[x, y] if e is not None else None
        for ((x, y), e) in expect_list]
    zipped = list(
        ((x, y), e, a, d)
        for (((x, y), e), a, d)
        in zip(expect_list, actual_list, difference_list))
    fudged = [
        ((x, y), e if e is None or d < threshold else a)
        for ((x, y), e, a, d) in zipped]
    assert expect_list == fudged


# Per Reiter (2004) Fig 2
def test_cell_example():
    #               1.000         1.000         1.000
    #        0.500         1.000         1.000         1.000
    # 0.200         0.500         1.000         1.000         1.000
    #        0.200         0.200         0.500         1.000
    #               0.200         0.200         0.500
    initial_state = make_state([
            [ None , None, 1.000, 1.000, 1.000,],
            [ None, 1.000, 1.000, 1.000, 1.000,],
            [1.000, 1.000, 1.000, 0.500, 0.500,],
            [0.500, 0.500, 0.200, 0.200,  None,],
            [0.200, 0.200, 0.200,  None,  None,],
        ], None)

    #               1.100         1.100         1.100
    #        0.617         1.100         1.100         1.100
    # 0.150         0.633         1.100         1.100         1.100
    #        0.617         0.350         0.617         1.100
    #               0.183         0.150         0.633
    expected_state = make_state([
            [ None,  None, 1.100, 1.100, 1.100,],
            [ None, 1.100, 1.100, 1.100, 1.100,],
            [1.100, 1.100, 1.100, 0.617, 0.633,],
            [0.617, 0.633, 0.350, 0.150,  None,],
            [0.150, 0.617, 0.183,  None,  None,],
        ], None)

    assert_state_equal(expected_state, transition(initial_state))
