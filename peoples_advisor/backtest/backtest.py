from datetime import datetime
from pathlib import Path
from queue import PriorityQueue
from threading import Event

from peoples_advisor.backtest.oanda.oanda_backtest import (
    OandaBacktestingData,
    OandaBacktestingGen,
)
from peoples_advisor.settings import (
    BROKER,
    API_TOKEN,
    INSTRUMENTS,
    ACCOUNT_CURRENCY,
)


def backtesting_gen_factory(priority_queue: PriorityQueue, run_flag: Event, data_path: Path):
    if BROKER == "OANDA":
        return OandaBacktestingGen(priority_queue, run_flag, data_path)
    else:
        return


def historical_gen_factory(
    from_time: datetime,
    to_time: datetime,
    granularity: str = None,
    filename: str = None,
):
    if BROKER == "OANDA":
        return OandaBacktestingData(
            API_TOKEN,
            INSTRUMENTS,
            ACCOUNT_CURRENCY,
            from_time,
            to_time,
            granularity,
            filename,
        )
    else:
        return
