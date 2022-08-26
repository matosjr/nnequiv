from nnenum.util import FreezableMeta

class Settings(metaclass=FreezableMeta):
    EQUIV_STRATEGIES = [
        "DONT",
        "CEGAR",
        "SECOND_NET",
        "REFINE_UNTIL_MAX",
        "REFINE_UNTIL_95P",
        "REFINE_UNTIL_LAST",
        "REFINE_UNTIL_LAST_OPTIMISTIC1",
        "REFINE_UNTIL_LAST_OPTIMISTIC2",
    ]
    
    @classmethod
    def reset(cls):
        "assign default settings"
        # EQUIV
        # 'DONT', 'CEGAR', 'SECOND_NET', 'REFINE_UNTIL_MAX', 'REFINE_UNTIL_95P', 'REFINE_UNTIL_LAST'
        cls.EQUIV_OVERAPPROX_STRAT = "REFINE_UNTIL_MAX"
        cls.EQUIV_OVERAPPROX_STRAT_MOVING_WINDOW = 300
        cls.EQUIV_OVERAPPROX_STRAT_REFINE_UNTIL = False