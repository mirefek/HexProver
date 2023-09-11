from goal import *

def thibault_position(env):
    env.make_blue_move((4, 3))
    yield True
    env.make_red_move((3, 4))
    yield True
    env.make_blue_move((4, 4))
    yield True
    env.make_red_move((3, 5))
    yield True
    env.make_blue_move((4, 5))
    yield True
    env.make_red_move((5, 1))
    yield True
    env.make_blue_move((4, 2))
    yield True
    env.make_red_move((4, 1))
    yield True
    env.make_blue_move((2, 2))
    yield True
    env.make_red_move((3, 2))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 1), False)
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((4, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_blue_move((4, 2))
    yield True
    env.make_red_move((4, 1))
    yield True
    env.make_blue_move((2, 2))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.make_blue_move((1, 5))
    yield True
    assert env.pop_stack()
    yield True
    env.make_blue_move((1, 4))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_blue_move((0, 4))
    yield True
    assert env.pop_stack()
    yield True
    env.make_blue_move((0, 4))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 3))
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((3, 2))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 6))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((1, 6))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((2, 6))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((2, 3))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 1))
    yield True
    env.split_node((2, 1), True)
    yield True
    env.make_red_move((2, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((3, 1))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 0))
    yield True
    env.split_node((1, 0), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 0), False)
    yield True
    env.make_red_move((2, 0))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.make_red_move((0, 0))
    yield True
    env.make_red_move((0, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((0, 1))
    yield True
    env.make_red_move((1, 2))
    yield True
    env.make_red_move((0, 2))
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((3, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((2, 2))
    yield True
    env.split_node((2, 2), True)
    yield True
    env.make_red_move((3, 1))
    yield True
    env.split_node((3, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((3, 2))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 2), False)
    yield True
    env.make_red_move((3, 1))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    env.make_red_move((0, 1))
    yield True
    env.make_red_move((0, 2))
    yield True
    env.make_red_move((2, 1))
    yield True
    env.make_red_move((1, 2))
    yield True
    env.make_red_move((3, 1))
    yield True
    env.make_red_move((1, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_blue_move((1, 2))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_blue_move((1, 3))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_blue_move((0, 5))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((1, 6))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((2, 6))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    env.make_red_move((1, 3))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    env.make_red_move((0, 1))
    yield True
    env.make_red_move((0, 2))
    yield True
    env.make_red_move((2, 1))
    yield True
    env.make_red_move((1, 2))
    yield True
    env.make_red_move((2, 1))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 1))
    yield True
    env.split_node((2, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 4))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 1))
    yield True
    env.split_node((2, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 4), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 2))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((2, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((2, 1))
    yield True
    env.split_node((2, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((2, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 2))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    env.make_red_move((4, 5))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((5, 6))
    yield True
    env.split_node((5, 6), True)
    yield True
    env.make_red_move((5, 5))
    yield True
    env.make_red_move((4, 6))
    yield True
    env.make_red_move((6, 5))
    yield True
    env.make_red_move((6, 6))
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 5))
    yield True
    env.split_node((4, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((4, 5), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_blue_move((3, 2))
    yield True
    env.make_red_move((4, 2))
    yield True
    env.split_node((3, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 3), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 3), False)
    yield True
    env.make_blue_move((5, 2))
    yield True
    env.make_red_move((5, 1))
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.split_node((5, 3), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 4), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((2, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.internal_connection((1, 4), (3, 3))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 5))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 4), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((4, 5))
    yield True
    env.split_node((4, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((5, 5))
    yield True
    env.split_node((5, 5), True)
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((4, 5))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((6, 5))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    env.make_blue_move((1, 5))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 3))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 4), True)
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 5))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((4, 5))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 4))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 1))
    yield True
    env.split_node((2, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 1))
    yield True
    env.split_node((2, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((4, 4), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((4, 4), False)
    yield True
    env.make_red_move((5, 5))
    yield True
    env.split_node((5, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 5), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 3))
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 4))
    yield True
    env.split_node((3, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 4), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 4), False)
    yield True
    env.make_blue_move((4, 2))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.split_node((5, 3), True)
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_red_move((4, 4))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((4, 4))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    env.make_red_move((6, 1))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((4, 2))
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.split_node((5, 4), True)
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((4, 4))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((1, 4))
    yield True
    env.split_node((1, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 4), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 4))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((2, 4))
    yield True
    env.make_blue_move((0, 5))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.internal_connection((2, 2), (3, 3))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.split_node((3, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 3), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 3), True)
    yield True
    env.make_blue_move((0, 4))
    yield True
    assert env.pop_stack()
    yield True
    env.make_blue_move((1, 1))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    env.make_red_move((0, 1))
    yield True
    env.make_red_move((0, 2))
    yield True
    env.make_red_move((2, 1))
    yield True
    env.make_red_move((1, 2))
    yield True
    env.make_blue_move((4, 3))
    yield True
    env.make_red_move((4, 2))
    yield True
    env.make_blue_move((6, 1))
    yield True
    env.make_red_move((5, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_blue_move((6, 1))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.split_node((5, 4), True)
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 4), False)
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((3, 5))
    yield True
    env.split_node((3, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 5), False)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.make_red_move((4, 5))
    yield True
    env.make_red_move((3, 4))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((5, 1))
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_blue_move((6, 2))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.split_node((5, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((5, 4))
    yield True
    env.split_node((5, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((2, 5))
    yield True
    env.split_node((2, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 5), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((1, 6))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((1, 5))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((1, 5))
    yield True
    env.split_node((1, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 5), True)
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_blue_move((4, 3))
    yield True
    env.make_red_move((4, 2))
    yield True
    env.make_blue_move((6, 1))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.split_node((5, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 4), False)
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((3, 5))
    yield True
    env.split_node((3, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 5), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((5, 1))
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((4, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), False)
    yield True
    env.make_blue_move((0, 5))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 2), True)
    yield True
    env.make_red_move((2, 2))
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 1), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((4, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((5, 3))
    yield True
    env.split_node((5, 3), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.split_node((2, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 5), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((2, 5), True)
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((1, 6))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((4, 3))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    env.make_red_move((3, 4))
    yield True
    env.make_red_move((3, 5))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((5, 5))
    yield True
    env.split_node((5, 5), True)
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((4, 5))
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_blue_move((6, 2))
    yield True
    env.make_red_move((5, 5))
    yield True
    env.split_node((5, 5), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 5), False)
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((6, 5))
    yield True
    env.make_red_move((3, 6))
    yield True
    env.split_node((3, 6), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((3, 6), False)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.split_node((5, 3), True)
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_red_move((4, 4))
    yield True
    env.make_red_move((3, 4))
    yield True
    env.make_red_move((3, 5))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((6, 3))
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((4, 5))
    yield True
    env.split_node((4, 5), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 5))
    yield True
    env.split_node((4, 5), True)
    yield True
    env.make_red_move((3, 5))
    yield True
    env.make_red_move((4, 4))
    yield True
    env.make_red_move((3, 4))
    yield True
    env.make_red_move((4, 3))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.split_node((4, 4), True)
    yield True
    env.make_red_move((3, 4))
    yield True
    env.make_red_move((3, 5))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 5))
    yield True
    env.split_node((5, 5), True)
    yield True
    env.make_red_move((5, 4))
    yield True
    env.make_red_move((4, 5))
    yield True
    env.make_red_move((6, 4))
    yield True
    env.make_red_move((6, 5))
    yield True
    env.make_red_move((4, 2))
    yield True
    env.make_blue_move((6, 1))
    yield True
    env.make_red_move((5, 4))
    yield True
    env.split_node((5, 4), True)
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((4, 2))
    yield True
    env.split_node((4, 2), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((4, 2), False)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_blue_move((0, 5))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    env.make_red_move((0, 1))
    yield True
    env.make_red_move((0, 2))
    yield True
    env.make_red_move((1, 2))
    yield True
    env.make_red_move((2, 1))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((3, 1))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.make_red_move((4, 1))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((4, 2))
    yield True
    env.split_node((4, 2), True)
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((5, 1))
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 3))
    yield True
    env.split_node((5, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 3), False)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((5, 3), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    env.make_red_move((3, 2))
    yield True
    env.split_node((3, 2), True)
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((2, 2))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    env.make_red_move((0, 1))
    yield True
    env.make_red_move((0, 2))
    yield True
    env.make_red_move((2, 1))
    yield True
    env.make_red_move((1, 2))
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((4, 1))
    yield True
    env.make_red_move((4, 2))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((4, 1))
    yield True
    env.make_red_move((4, 2))
    yield True
    env.make_red_move((6, 0))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((5, 2))
    yield True
    env.split_node((5, 2), True)
    yield True
    env.make_red_move((4, 2))
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_red_move((6, 1))
    yield True
    env.make_red_move((6, 2))
    yield True
    env.make_red_move((4, 3))
    yield True
    env.make_blue_move((5, 2))
    yield True
    env.make_red_move((4, 5))
    yield True
    env.split_node((4, 5), True)
    yield True
    env.make_red_move((4, 4))
    yield True
    env.make_red_move((3, 5))
    yield True
    env.make_red_move((2, 5))
    yield True
    env.make_red_move((3, 4))
    yield True
    assert env.close_with_lemma(True)
    yield True
    env.make_red_move((5, 1))
    yield True
    env.split_node((5, 1), True)
    yield True
    assert env.close_with_fork()
    yield True
    assert env.close_with_fork()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((4, 1))
    yield True
    env.internal_connection((3, 3), (4, 1))
    yield True
    env.make_red_move((3, 2))
    yield True
    env.make_red_move((4, 2))
    yield True
    env.split_node((2, 4), True)
    yield True
    env.make_red_move((0, 5))
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((1, 5))
    yield True
    env.make_red_move((0, 6))
    yield True
    env.make_red_move((1, 3))
    yield True
    env.split_node((1, 3), True)
    yield True
    assert env.pop_stack()
    yield True
    env.split_node((1, 3), False)
    yield True
    env.make_red_move((1, 4))
    yield True
    env.make_red_move((2, 3))
    yield True
    env.make_red_move((0, 4))
    yield True
    env.make_red_move((1, 1))
    yield True
    env.split_node((1, 1), True)
    yield True
    env.make_red_move((0, 1))
    yield True
    env.make_red_move((0, 2))
    yield True
    env.make_red_move((1, 2))
    yield True
    env.make_red_move((3, 0))
    yield True
    env.split_node((3, 0), True)
    yield True
    env.make_red_move((2, 0))
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    assert env.pop_stack()
    yield True
    env.make_red_move((2, 1))
    yield True
    env.make_red_move((2, 2))
    yield False

if __name__ == "__main__":
    diagram = HexDiagram.parse("""
    ---------------------------
     .   .   .   .   .   .   . 
       .   .   .   .   .   .   . 
         .   .   .   .   .   .   . 
           .   .   .   O   .   .   . 
             .   .   .   .   .   .   . 
               .   .   .   .   .   .   . 
                 .   .   .   .   .   .   . 
                ---------------------------
    """)
    env = GoalEnv(diagram)

    thibault_position(env)
