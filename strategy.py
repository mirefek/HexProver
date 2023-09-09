from collections import defaultdict
from weakref import WeakValueDictionary

class StrategyCases:
    def __init__(self, node_tuple, nodes, blue_to_action):
        self.node_tuple = node_tuple # node -> index
        self.nodes = nodes
        self.blue_to_action = blue_to_action # all in index coordinates

    def map_nodes(self, homo):
        if all(homo[n] == n for n in self.nodes): return self
        return strategy_cases(
            tuple(homo[n] for n in self.node_tuple),
            self.blue_to_action
        )

    def ignore_nodes(self, nodes):
        to_ignore = [i for i,n in enumerate(self.node_tuple) if n in nodes]
        if len(to_ignore) == len(self.node_tuple): return None
        actions = list(set(self.blue_to_action))
        action_to_i = { action : i for i,action in enumerate(actions) }
        action_i_to_blues = [set() for action in actions]
        for blue, action in enumerate(self.blue_to_action):
            action_i_to_blues[action_to_i[action]].add(blue)
        node_i_to_action_i = [action_to_i[self.blue_to_action[ni]] for ni in range(len(self.node_tuple))]

        to_ignore = set(to_ignore)
        for blues in action_i_to_blues:
            blues.difference_update(to_ignore)
        next_actions = []
        for action, blues in zip(actions, action_i_to_blues):
            red, strategy = action
            if red not in to_ignore:
                strategy = strategy.ignore_nodes(to_ignore)
                next_actions.append((red, strategy))
            else:
                remaining_strategy_nodes = strategy.nodes - to_ignore
                if not remaining_strategy_nodes:
                    return None
                else:
                    red = min(remaining_strategy_nodes)
                    strategy = strategy.ignore_nodes(to_ignore | set([red]))
                    next_actions.append((red, strategy))
        actions = next_actions

        new_to_ori = [
            ni
            for ni in range(len(self.node_tuple))
            if self.node_tuple[ni] not in to_ignore
        ]

        ori_to_new = [0]*len(self.node_tuple)
        for new,ori in enumerate(new_to_ori):
            ori_to_new[ori] = new

        next_actions = []
        for blue, (red, strategy) in enumerate(actions):
            strategy = strategy.map_nodes(ori_to_new)
            next_actions.append((ori_to_new[red], strategy))
        actions = next_actions

        node_tuple = [self.node_tuple[ori] for ori in new_to_ori]
        blue_to_action = [actions[node_i_to_action_i[ori]] for ori in new_to_ori]
        return strategy_cases(node_tuple, blue_to_action)

class StrategyCombined:
    def __init__(self, strategies, nodes):
        self.strategies = strategies
        self.nodes = nodes

    def map_nodes(self, homo):
        if all(homo[n] == n for n in self.nodes): return self
        # disjoint check
        img = set(
            homo[x]
            for x in self.nodes
        )
        assert len(img) == len(self.nodes)
            
        return strategy_combined(
            strategy.map_nodes(homo)
            for strategy in self.strategies
        )

    def to_state(self, homo):
        blue_to_strategy = dict()
        for strategy in self.strategies:
            for blue in strategy.nodes:
                blue_to_strategy[blue] = strategy
        return StrategyState(blue_to_strategy)

    def __or__(self, other):
        if other.strategies <= self.strategies: return self
        elif self.strategies <= other.strategies: return other
        return strategy_combined(self.strategies | other.strategies)

    def respond(self, blue):
        if blue not in self.nodes: return None, self

        for substrategy in self.strategies:
            if blue not in substrategy.nodes: continue
            blue_local = substrategy.node_tuple.index(blue)
            for b,(red_local, next_strategy) in enumerate(substrategy.blue_to_action):
                if b == blue_local: break
            else:
                raise Exception("Internal error")
            red = substrategy.node_tuple[red_local]
            next_strategy = next_strategy.map_nodes(substrategy.node_tuple)
            if len(self.strategies) == 1: return red, next_strategy
            else:
                strategies = (self.strategies - frozenset([substrategy])) | next_strategy.strategies
                return red, strategy_combined(strategies)
        else:
            raise Exception("Internal error -- strategy nodes inconsistency")

    def ignore_nodes(self, nodes):
        nodes = frozenset(nodes) & self.nodes
        if not nodes: return self
        strategies = [
            strategy.ignore_nodes(nodes)
            for strategy in self.strategies
        ]
        return strategy_combined(filter(lambda x: x is not None, strategies))

_strategy_cases_cache = WeakValueDictionary()
_strategy_combined_cache = WeakValueDictionary()

# preferred constructors
def strategy_cases(node_tuple, blue_to_action):
    node_tuple = tuple(node_tuple)
    blue_to_action = tuple(blue_to_action)
    res = _strategy_cases_cache.get((node_tuple, blue_to_action))
    if res is not None: return res

    assert len(node_tuple) == len(blue_to_action)
    num_nodes = len(node_tuple)
    nodes = set(node_tuple)

    # sanity checks
    assert len(nodes) == num_nodes # no duplicities
    local_nodes = set(range(num_nodes))
    action_to_blue = defaultdict(set)
    for blue, action in enumerate(blue_to_action):
        action_to_blue[action].add(blue)
    for (red, strategy), blues in action_to_blue.items():
        assert isinstance(strategy, StrategyCombined)
        assert red not in blues, (red, strategy.nodes, blues)
        assert not (strategy.nodes & blues), (red, strategy.nodes, blues)
        assert strategy.nodes <= set(local_nodes)

    res = StrategyCases(node_tuple, nodes, blue_to_action)
    _strategy_cases_cache[node_tuple, blue_to_action] = res
    return res

def strategy_combined(strategies):
    strategies = frozenset(strategies)
    res = _strategy_cases_cache.get(strategies)
    if res is not None: return res    

    assert all(isinstance(strategy, StrategyCases) for strategy in strategies)
    nodes = set()
    for strategy in strategies:
        assert not (nodes & strategy.nodes)
        nodes |= strategy.nodes
    res = StrategyCombined(strategies, nodes)
    _strategy_cases_cache[strategies] = res
    return res

empty_strategy = strategy_combined(())
