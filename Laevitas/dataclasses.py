from dataclasses import dataclass, field
from typing import List


# analytic options:
# get_atm
@dataclass
class MaturityIV:
    maturity: str
    iv: float


@dataclass
class data_atm:
    datajson: list
    date: int
    Today: List[MaturityIV] = field(default_factory=lambda: [])
    Yesterday: List[MaturityIV] = field(default_factory=lambda: [])
    Two_days_ago: List[MaturityIV] = field(default_factory=lambda: [])
    One_week_ago: List[MaturityIV] = field(default_factory=lambda: [])
    Two_weeks_ago: List[MaturityIV] = field(default_factory=lambda: [])
    Three_weeks_ago: List[MaturityIV] = field(default_factory=lambda: [])


# gex_date_all
@dataclass
class gex_date_all_data:
    strike: int
    optionType: str
    gex: float


@dataclass
class Igex_date_all:
    datajson: list
    date: int
    data: List[gex_date_all_data] = field(default_factory=lambda: [])


# gex_date
@dataclass
class gex_date_data:
    strike: int
    optionType: str
    gex: float


@dataclass
class Igex_date:
    datajson: list
    date: int
    data: List[gex_date_data] = field(default_factory=lambda: [])


# oi_expiry
@dataclass
class expiry_data:
    maturity: str
    c: float
    p: float
    notional_c: float
    notional_p: float


@dataclass
class Iexpiry:
    datajson: list
    date: int
    data: List[expiry_data] = field(default_factory=lambda: [])


# oi_strike_all
@dataclass
class oi_strike_all_data:
    strike: int
    c: float
    p: float
    notional_c: float
    notional_p: float


@dataclass
class Ioi_strike_all:
    datajson: list
    date: int
    data: List[oi_strike_all_data] = field(default_factory=lambda: [])


#top_traded_option
@dataclass
class top_traded_option_data:
    volume: float
    instrument: str
    volume_usd: float


@dataclass
class Itop_traded_option:
    datajson: list
    date: int
    data: List[top_traded_option_data] = field(default_factory=lambda: [])


# v_strike_all
@dataclass
class v_strike_all_data:
    strike: int
    C: float
    P: float
    USDVC: float
    USDVP: float


@dataclass
class v_strike_alli:
    datajson: list
    date: int
    data: List[v_strike_all_data] = field(default_factory=lambda: [])



# greeks
@dataclass
class greeks_data:
    strike: int
    underlying_price: float
    delta: float
    gamma: float
    theta: float
    vega: float


@dataclass
class Igreeks:
    datajson: list
    date: int
    data: List[greeks_data] = field(default_factory=lambda: [])


# realtime/derivs
# oi_gainers
@dataclass
class oi_gainers_data:
    symbol: str
    open_interest_change: int
    open_interest_change_notional: int


@dataclass
class Ioi_gainers:
    datajson: list
    date: int
    data: List[oi_gainers_data] = field(default_factory=lambda: [])


# historical


@dataclass
class Ipaginationmeta:
    total: int
    page: int
    items: int

# historical/options
# iv


@dataclass
class ivdata:
    date: int
    mark_iv: float
    bid_iv: float
    ask_iv: float


@dataclass
class Ipaginationiv:
    datajson: list
    meta: Ipaginationmeta
    items: List[ivdata] = field(default_factory=lambda: [])


#iv_bid_ask
@dataclass
class iv_bid_ask_data:
    ask: float
    bid: float
    mark: float


@dataclass
class IpaginationIv_bid_ask:
    datajson: list
    meta: Ipaginationmeta
    date: List[int] = field(default_factory=lambda: [])
    week: List[iv_bid_ask_data] = field(default_factory=lambda: [])
    two_weeks: List[iv_bid_ask_data] = field(default_factory=lambda: [])
    one_month: List[iv_bid_ask_data] = field(default_factory=lambda: [])
    two_months: List[iv_bid_ask_data] = field(default_factory=lambda: [])
    half_a_year: List[iv_bid_ask_data] = field(default_factory=lambda: [])
    year: List[iv_bid_ask_data] = field(default_factory=lambda: [])

# historical/moves
# total_oi

@dataclass
class IDateV:
    v: float
    date: int


@dataclass
class Ipagination:
    datajson: list
    meta: Ipaginationmeta
    items: List[IDateV] = field(default_factory=lambda: [])
