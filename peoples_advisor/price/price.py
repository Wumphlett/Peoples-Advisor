from queue import PriorityQueue
from threading import Event

from peoples_advisor.price.oanda.oanda_price import OandaPricingGen
from peoples_advisor.settings import (
    BROKER,
    API_TOKEN,
    LIVE,
    ACCOUNT_INDEX,
    DATETIME_FORMAT,
    INSTRUMENTS,
    ACCOUNT_CURRENCY,
    SAVE_LIVE_AS_HISTORICAL,
)


def pricing_gen_factory(priority_queue: PriorityQueue, exit_flag: Event):
    if BROKER == "OANDA":
        return OandaPricingGen(
            API_TOKEN,
            LIVE,
            ACCOUNT_INDEX,
            DATETIME_FORMAT,
            INSTRUMENTS,
            ACCOUNT_CURRENCY,
            priority_queue,
            exit_flag,
            SAVE_LIVE_AS_HISTORICAL,
        )
    else:
        return
