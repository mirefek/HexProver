from goal import *

def thibault_position(env):
    env.make_blue_move((4, 3))
    env.make_red_move((3, 4))
    env.make_blue_move((4, 4))
    env.make_red_move((3, 5))
    env.make_blue_move((4, 5))
    env.make_red_move((5, 1))
    env.make_blue_move((4, 2))
    env.make_red_move((4, 1))
    env.make_blue_move((2, 2))
    env.make_red_move((3, 2))
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((5, 1), True)
    assert env.pop_stack()
    env.split_node((5, 1), False)
    env.make_red_move((6, 0))
    env.make_red_move((6, 1))
    env.make_red_move((4, 2))
    assert env.pop_stack()
    env.make_blue_move((4, 2))
    env.make_red_move((4, 1))
    env.make_blue_move((2, 2))
    env.make_red_move((3, 2))
    env.make_blue_move((1, 5))
    assert env.pop_stack()
    env.make_blue_move((1, 4))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((2, 4))
    env.make_red_move((2, 5))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    env.make_red_move((0, 6))
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    env.make_red_move((0, 3))
    env.make_red_move((0, 4))
    env.make_red_move((1, 4))
    env.make_red_move((2, 3))
    env.make_red_move((2, 4))
    env.make_red_move((2, 5))
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 3))
    env.make_blue_move((0, 4))
    assert env.pop_stack()
    env.make_blue_move((0, 4))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 3))
    assert env.close_with_fork()
    env.make_red_move((3, 2))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.close_with_fork()
    env.make_red_move((2, 4))
    env.make_red_move((2, 5))
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    env.make_red_move((0, 4))
    env.make_red_move((0, 6))
    env.make_red_move((1, 6))
    assert env.pop_stack()
    env.make_red_move((1, 5))
    env.make_red_move((1, 6))
    env.make_red_move((2, 5))
    env.make_red_move((2, 6))
    env.make_red_move((2, 3))
    env.make_red_move((2, 4))
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    env.make_red_move((2, 2))
    env.make_red_move((2, 3))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((1, 3), False)
    env.make_red_move((2, 2))
    env.make_red_move((2, 3))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((1, 4))
    env.make_red_move((2, 5))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((0, 4))
    env.make_red_move((3, 2))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 1))
    env.split_node((2, 1), True)
    env.make_red_move((2, 2))
    assert env.pop_stack()
    env.make_red_move((2, 2))
    env.make_red_move((3, 1))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((2, 1), False)
    assert env.close_with_fork()
    env.make_red_move((1, 0))
    env.split_node((1, 0), True)
    assert env.pop_stack()
    env.split_node((1, 0), False)
    env.make_red_move((2, 0))
    env.make_red_move((1, 1))
    env.make_red_move((0, 0))
    env.make_red_move((0, 2))
    assert env.pop_stack()
    env.make_red_move((0, 1))
    env.make_red_move((1, 2))
    env.make_red_move((0, 2))
    env.make_red_move((0, 3))
    env.make_red_move((3, 2))
    assert env.pop_stack()
    env.make_red_move((2, 2))
    env.split_node((2, 2), True)
    env.make_red_move((3, 1))
    env.split_node((3, 3), True)
    assert env.pop_stack()
    env.make_red_move((3, 2))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((2, 2), False)
    env.make_red_move((3, 1))
    env.make_red_move((3, 2))
    env.make_red_move((1, 3))
    env.make_red_move((0, 3))
    env.make_red_move((0, 4))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    env.make_red_move((0, 1))
    env.make_red_move((0, 2))
    env.make_red_move((2, 1))
    env.make_red_move((1, 2))
    env.make_red_move((3, 1))
    env.make_red_move((1, 2))
    assert env.pop_stack()
    env.make_blue_move((1, 2))
    env.make_red_move((2, 2))
    env.make_blue_move((1, 3))
    env.make_red_move((2, 3))
    env.make_blue_move((0, 5))
    env.make_red_move((1, 4))
    env.make_red_move((0, 4))
    env.make_red_move((0, 6))
    env.make_red_move((1, 5))
    env.make_red_move((1, 6))
    env.make_red_move((2, 5))
    env.make_red_move((2, 6))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((1, 4))
    env.make_red_move((2, 4))
    env.make_red_move((1, 4))
    env.make_red_move((0, 4))
    env.make_red_move((0, 5))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 3))
    env.make_red_move((0, 3))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.pop_stack()
    env.split_node((1, 5), True)
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((1, 4))
    env.make_red_move((2, 3))
    env.make_red_move((2, 4))
    env.make_red_move((2, 5))
    env.make_red_move((1, 3))
    env.make_red_move((0, 3))
    env.make_red_move((0, 4))
    env.make_red_move((2, 2))
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    env.make_red_move((1, 3))
    assert env.pop_stack()
    env.make_red_move((0, 4))
    env.make_red_move((0, 5))
    env.make_red_move((1, 3))
    env.make_red_move((2, 3))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    env.make_red_move((0, 1))
    env.make_red_move((0, 2))
    env.make_red_move((2, 1))
    env.make_red_move((1, 2))
    env.make_red_move((2, 1))
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.close_with_lemma(True)
    assert env.close_with_fork()
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_fork()
    env.make_red_move((2, 1))
    env.split_node((2, 1), True)
    assert env.pop_stack()
    env.split_node((2, 1), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    env.make_red_move((0, 4))
    env.make_red_move((1, 4))
    env.make_red_move((1, 3))
    env.make_red_move((2, 3))
    env.make_red_move((2, 2))
    env.make_red_move((0, 6))
    env.make_red_move((1, 4))
    assert env.pop_stack()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    env.make_red_move((0, 3))
    env.make_red_move((0, 4))
    env.make_red_move((2, 3))
    env.make_red_move((1, 4))
    env.make_red_move((0, 6))
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_fork()
    env.make_red_move((2, 1))
    env.split_node((2, 1), True)
    assert env.pop_stack()
    env.split_node((2, 1), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.pop_stack()
    env.split_node((1, 4), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_fork()
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 2))
    assert env.close_with_lemma(True)
    env.make_red_move((2, 2))
    assert env.pop_stack()
    env.make_red_move((2, 1))
    env.split_node((2, 1), True)
    assert env.pop_stack()
    env.split_node((2, 1), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((2, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((4, 2))
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.pop_stack()
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    env.make_red_move((4, 5))
    env.make_red_move((5, 4))
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    env.make_red_move((5, 6))
    env.split_node((5, 6), True)
    env.make_red_move((5, 5))
    env.make_red_move((4, 6))
    env.make_red_move((6, 5))
    env.make_red_move((6, 6))
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((2, 4))
    env.make_red_move((2, 5))
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    env.make_red_move((0, 3))
    env.make_red_move((0, 4))
    env.make_red_move((2, 2))
    env.make_red_move((2, 3))
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((4, 5))
    env.split_node((4, 5), True)
    assert env.pop_stack()
    env.split_node((4, 5), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_blue_move((3, 2))
    env.make_red_move((4, 2))
    env.split_node((3, 3), True)
    assert env.pop_stack()
    env.split_node((3, 3), False)
    assert env.pop_stack()
    env.split_node((3, 3), True)
    assert env.pop_stack()
    env.split_node((3, 3), False)
    env.make_blue_move((5, 2))
    env.make_red_move((5, 1))
    env.make_red_move((6, 0))
    env.make_red_move((6, 1))
    env.make_red_move((5, 3))
    env.split_node((5, 3), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.pop_stack()
    env.split_node((1, 4), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    env.make_red_move((0, 3))
    env.make_red_move((0, 4))
    env.make_red_move((2, 3))
    env.make_red_move((1, 4))
    env.make_red_move((0, 6))
    env.make_red_move((2, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.pop_stack()
    env.internal_connection((1, 4), (3, 3))
    env.make_red_move((2, 3))
    env.make_red_move((2, 4))
    env.make_red_move((0, 4))
    env.make_red_move((0, 5))
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((1, 4), True)
    assert env.pop_stack()
    env.split_node((1, 4), False)
    assert env.pop_stack()
    env.split_node((1, 4), True)
    assert env.close_with_fork()
    env.make_red_move((4, 5))
    env.split_node((4, 5), True)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((4, 4))
    env.make_red_move((6, 3))
    env.make_red_move((5, 3))
    env.make_red_move((5, 4))
    env.make_red_move((5, 4))
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    env.make_red_move((5, 3))
    env.make_red_move((6, 2))
    env.make_red_move((6, 3))
    env.make_red_move((5, 5))
    env.split_node((5, 5), True)
    env.make_red_move((5, 4))
    env.make_red_move((4, 5))
    env.make_red_move((6, 4))
    env.make_red_move((6, 5))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.pop_stack()
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    env.make_blue_move((1, 5))
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.close_with_fork()
    env.make_red_move((2, 3))
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((1, 4), True)
    env.make_red_move((2, 3))
    env.make_red_move((2, 4))
    env.make_red_move((0, 4))
    env.make_red_move((0, 5))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    env.make_red_move((2, 4))
    env.make_red_move((2, 5))
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((4, 5))
    assert env.close_with_lemma(True)
    env.make_red_move((4, 4))
    assert env.close_with_lemma(True)
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.close_with_lemma(True)
    assert env.close_with_fork()
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 1))
    env.split_node((2, 1), True)
    assert env.pop_stack()
    env.split_node((2, 1), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 2))
    env.make_red_move((0, 4))
    env.make_red_move((1, 3))
    env.make_red_move((1, 4))
    env.make_red_move((2, 3))
    env.make_red_move((2, 4))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    assert env.pop_stack()
    env.split_node((1, 1), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 1))
    env.split_node((2, 1), True)
    assert env.pop_stack()
    env.split_node((2, 1), False)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.close_with_lemma(True)
    assert env.close_with_fork()
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.pop_stack()
    env.split_node((4, 4), False)
    assert env.close_with_lemma(True)
    assert env.close_with_lemma(True)
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.pop_stack()
    env.split_node((4, 4), False)
    env.make_red_move((5, 5))
    env.split_node((5, 5), True)
    assert env.pop_stack()
    env.split_node((5, 5), False)
    assert env.pop_stack()
    env.split_node((5, 5), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    env.make_red_move((2, 3))
    assert env.close_with_fork()
    env.make_red_move((0, 6))
    env.make_red_move((0, 5))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    env.make_red_move((0, 6))
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    env.make_red_move((2, 3))
    env.make_red_move((1, 4))
    env.make_red_move((0, 3))
    env.make_red_move((0, 4))
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((3, 4))
    env.split_node((3, 4), True)
    assert env.pop_stack()
    env.split_node((3, 4), False)
    assert env.pop_stack()
    env.split_node((3, 4), True)
    assert env.pop_stack()
    env.split_node((3, 4), False)
    env.make_blue_move((4, 2))
    env.make_red_move((5, 3))
    env.split_node((5, 3), True)
    env.make_red_move((4, 3))
    env.make_red_move((4, 4))
    env.make_red_move((6, 2))
    env.make_red_move((6, 3))
    env.make_red_move((4, 4))
    assert env.close_with_lemma(True)
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    env.make_red_move((6, 1))
    assert env.pop_stack()
    env.make_red_move((4, 2))
    env.make_red_move((4, 3))
    env.make_red_move((6, 1))
    env.make_red_move((5, 4))
    env.split_node((5, 4), True)
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((5, 3))
    env.make_red_move((4, 4))
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.close_with_fork()
    env.make_red_move((0, 6))
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((1, 4))
    env.split_node((1, 4), True)
    assert env.pop_stack()
    env.split_node((1, 4), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((3, 4))
    assert env.pop_stack()
    env.make_red_move((2, 4))
    env.make_blue_move((0, 5))
    env.make_red_move((2, 2))
    env.internal_connection((2, 2), (3, 3))
    env.make_red_move((3, 2))
    env.make_red_move((2, 3))
    env.split_node((3, 3), True)
    assert env.pop_stack()
    env.split_node((3, 3), False)
    assert env.pop_stack()
    env.split_node((3, 3), True)
    env.make_blue_move((0, 4))
    assert env.pop_stack()
    env.make_blue_move((1, 1))
    env.make_red_move((0, 4))
    env.make_red_move((1, 3))
    env.make_red_move((1, 4))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    env.make_red_move((0, 1))
    env.make_red_move((0, 2))
    env.make_red_move((2, 1))
    env.make_red_move((1, 2))
    env.make_blue_move((4, 3))
    env.make_red_move((4, 2))
    env.make_blue_move((6, 1))
    env.make_red_move((5, 2))
    assert env.pop_stack()
    env.make_blue_move((6, 1))
    env.make_red_move((5, 4))
    env.split_node((5, 4), True)
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((5, 4), False)
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    env.make_red_move((3, 5))
    env.split_node((3, 5), True)
    assert env.pop_stack()
    env.split_node((3, 5), False)
    env.make_red_move((4, 4))
    env.make_red_move((4, 5))
    env.make_red_move((3, 4))
    env.make_red_move((2, 5))
    env.make_red_move((5, 2))
    env.make_red_move((6, 2))
    env.make_red_move((5, 3))
    env.make_red_move((5, 1))
    env.make_red_move((6, 0))
    env.make_red_move((6, 1))
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((4, 3))
    env.make_blue_move((6, 2))
    env.make_red_move((5, 4))
    env.split_node((5, 4), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((6, 2))
    env.make_red_move((5, 2))
    env.make_red_move((5, 3))
    env.make_red_move((5, 2))
    env.make_red_move((6, 1))
    env.make_red_move((6, 2))
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((4, 3))
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((5, 4))
    env.split_node((5, 4), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((2, 5))
    env.split_node((2, 5), True)
    assert env.pop_stack()
    env.split_node((2, 5), False)
    assert env.close_with_lemma(True)
    env.make_red_move((0, 6))
    env.make_red_move((1, 5))
    env.make_red_move((1, 6))
    env.make_red_move((1, 4))
    env.make_red_move((0, 4))
    env.make_red_move((0, 5))
    env.make_red_move((1, 5))
    assert env.pop_stack()
    env.make_red_move((1, 5))
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((1, 5))
    env.split_node((1, 5), True)
    assert env.pop_stack()
    env.split_node((1, 5), False)
    assert env.pop_stack()
    env.split_node((1, 5), True)
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_blue_move((4, 3))
    env.make_red_move((4, 2))
    env.make_blue_move((6, 1))
    env.make_red_move((5, 4))
    env.split_node((5, 4), True)
    assert env.pop_stack()
    env.split_node((5, 4), False)
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    env.make_red_move((5, 2))
    env.make_red_move((6, 2))
    env.make_red_move((5, 3))
    env.make_red_move((3, 5))
    env.split_node((3, 5), True)
    assert env.pop_stack()
    env.split_node((3, 5), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((5, 1))
    env.make_red_move((6, 0))
    env.make_red_move((6, 1))
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((4, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((4, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    assert env.pop_stack()
    env.split_node((3, 2), True)
    assert env.pop_stack()
    env.split_node((3, 2), False)
    env.make_blue_move((0, 5))
    env.make_red_move((2, 2))
    env.make_red_move((0, 4))
    env.make_red_move((1, 3))
    env.make_red_move((1, 4))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.split_node((3, 2), True)
    env.make_red_move((2, 2))
    assert env.pop_stack()
    env.make_red_move((2, 2))
    env.make_red_move((0, 4))
    env.make_red_move((1, 3))
    env.make_red_move((1, 4))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    assert env.pop_stack()
    env.split_node((1, 1), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((1, 4))
    env.make_red_move((0, 4))
    env.make_red_move((0, 5))
    env.make_red_move((1, 5))
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    assert env.close_with_lemma(True)
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((4, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    assert env.close_with_fork()
    env.make_red_move((5, 3))
    env.split_node((5, 3), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((6, 0))
    env.make_red_move((2, 5))
    env.split_node((2, 5), True)
    assert env.pop_stack()
    env.split_node((2, 5), False)
    assert env.pop_stack()
    env.split_node((2, 5), True)
    env.make_red_move((0, 6))
    env.make_red_move((1, 5))
    env.make_red_move((1, 6))
    env.make_red_move((1, 4))
    env.make_red_move((0, 5))
    env.make_red_move((0, 4))
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.close_with_fork()
    env.make_red_move((6, 3))
    env.make_red_move((5, 3))
    env.make_red_move((5, 4))
    env.make_red_move((5, 4))
    env.make_red_move((6, 3))
    env.make_red_move((6, 4))
    env.make_red_move((5, 3))
    env.make_red_move((6, 2))
    env.make_red_move((6, 3))
    env.make_red_move((4, 3))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    env.make_red_move((3, 4))
    env.make_red_move((3, 5))
    env.make_red_move((5, 3))
    env.make_red_move((6, 2))
    env.make_red_move((6, 3))
    env.make_red_move((5, 5))
    env.split_node((5, 5), True)
    env.make_red_move((5, 4))
    env.make_red_move((4, 5))
    assert env.close_with_fork()
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((4, 3))
    env.make_blue_move((6, 2))
    env.make_red_move((5, 5))
    env.split_node((5, 5), True)
    assert env.pop_stack()
    env.split_node((5, 5), False)
    env.make_red_move((6, 4))
    env.make_red_move((6, 5))
    env.make_red_move((3, 6))
    env.split_node((3, 6), True)
    assert env.pop_stack()
    env.split_node((3, 6), False)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((5, 3))
    env.make_red_move((6, 3))
    env.make_red_move((5, 4))
    env.make_red_move((6, 2))
    env.make_red_move((5, 2))
    env.make_red_move((5, 3))
    env.make_red_move((5, 2))
    env.make_red_move((6, 2))
    env.make_red_move((6, 1))
    env.make_red_move((5, 3))
    env.split_node((5, 3), True)
    env.make_red_move((4, 3))
    env.make_red_move((4, 4))
    env.make_red_move((3, 4))
    env.make_red_move((3, 5))
    env.make_red_move((6, 2))
    env.make_red_move((6, 3))
    env.make_red_move((4, 3))
    env.make_red_move((5, 2))
    env.make_red_move((6, 1))
    env.make_red_move((6, 2))
    env.make_red_move((4, 5))
    env.split_node((4, 5), True)
    assert env.close_with_fork()
    assert env.close_with_lemma(True)
    env.make_red_move((4, 5))
    env.split_node((4, 5), True)
    env.make_red_move((3, 5))
    env.make_red_move((4, 4))
    env.make_red_move((3, 4))
    env.make_red_move((4, 3))
    assert env.close_with_lemma(True)
    env.make_red_move((4, 4))
    env.split_node((4, 4), True)
    env.make_red_move((3, 4))
    env.make_red_move((3, 5))
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    env.make_red_move((4, 3))
    env.make_red_move((5, 3))
    env.make_red_move((6, 2))
    env.make_red_move((6, 1))
    env.make_red_move((5, 5))
    env.split_node((5, 5), True)
    env.make_red_move((5, 4))
    env.make_red_move((4, 5))
    env.make_red_move((6, 4))
    env.make_red_move((6, 5))
    env.make_red_move((4, 2))
    env.make_blue_move((6, 1))
    env.make_red_move((5, 4))
    env.split_node((5, 4), True)
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((4, 2))
    env.split_node((4, 2), True)
    assert env.pop_stack()
    env.split_node((4, 2), False)
    assert env.close_with_lemma(True)
    env.make_blue_move((0, 5))
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    env.make_red_move((2, 3))
    env.make_red_move((1, 4))
    env.make_red_move((0, 4))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    env.make_red_move((0, 1))
    env.make_red_move((0, 2))
    env.make_red_move((1, 2))
    env.make_red_move((2, 1))
    env.make_red_move((2, 2))
    env.make_red_move((3, 1))
    env.make_red_move((3, 2))
    env.make_red_move((4, 1))
    env.make_red_move((1, 5))
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((4, 2))
    env.split_node((4, 2), True)
    assert env.close_with_lemma(True)
    env.make_red_move((5, 1))
    env.make_red_move((6, 0))
    env.make_red_move((6, 1))
    env.make_red_move((5, 3))
    env.split_node((5, 3), True)
    assert env.pop_stack()
    env.split_node((5, 3), False)
    assert env.pop_stack()
    env.split_node((5, 3), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    env.make_red_move((3, 2))
    env.split_node((3, 2), True)
    env.make_red_move((1, 5))
    env.make_red_move((0, 5))
    env.make_red_move((0, 6))
    env.make_red_move((2, 2))
    env.make_red_move((0, 4))
    env.make_red_move((1, 3))
    env.make_red_move((1, 4))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    env.make_red_move((0, 1))
    env.make_red_move((0, 2))
    env.make_red_move((2, 1))
    env.make_red_move((1, 2))
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    env.make_red_move((6, 0))
    env.make_red_move((6, 1))
    env.make_red_move((4, 1))
    env.make_red_move((4, 2))
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((4, 1))
    env.make_red_move((4, 2))
    env.make_red_move((6, 0))
    env.make_red_move((6, 1))
    env.make_red_move((5, 2))
    env.split_node((5, 2), True)
    env.make_red_move((4, 2))
    env.make_red_move((4, 3))
    env.make_red_move((6, 1))
    env.make_red_move((6, 2))
    env.make_red_move((4, 3))
    env.make_blue_move((5, 2))
    env.make_red_move((4, 5))
    env.split_node((4, 5), True)
    env.make_red_move((4, 4))
    env.make_red_move((3, 5))
    env.make_red_move((2, 5))
    env.make_red_move((3, 4))
    assert env.close_with_lemma(True)
    env.make_red_move((5, 1))
    env.split_node((5, 1), True)
    assert env.close_with_fork()
    assert env.close_with_fork()
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((4, 1))
    env.internal_connection((3, 3), (4, 1))
    env.make_red_move((3, 2))
    env.make_red_move((4, 2))
    env.split_node((2, 4), True)
    env.make_red_move((0, 5))
    env.make_red_move((1, 4))
    env.make_red_move((1, 5))
    env.make_red_move((1, 5))
    env.make_red_move((0, 6))
    env.make_red_move((1, 3))
    env.split_node((1, 3), True)
    assert env.pop_stack()
    env.split_node((1, 3), False)
    env.make_red_move((1, 4))
    env.make_red_move((2, 3))
    env.make_red_move((0, 4))
    env.make_red_move((1, 1))
    env.split_node((1, 1), True)
    env.make_red_move((0, 1))
    env.make_red_move((0, 2))
    env.make_red_move((1, 2))
    env.make_red_move((3, 0))
    env.split_node((3, 0), True)
    env.make_red_move((2, 0))
    assert env.pop_stack()
    assert env.pop_stack()
    assert env.pop_stack()
    env.make_red_move((2, 1))
    env.make_red_move((2, 2))

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
