import QuantLib as ql

class Calculator(object):
    def __init__(self):
        self._calendar = ql.HongKong()
        self._day_count = ql.Actual365Fixed()
        self._option_type = ql.Option.Call

    def _set_calculation_date(self, yyyy_mm_dd):
        (yyyy,mm,dd) = yyyy_mm_dd
        calculation_date = ql.Date(dd, mm, yyyy)
        ql.Settings.instance().evaluationDate = calculation_date

    def _create_option(self, option_type, strike_price, maturity_yyyy_mm_dd):
        payoff = ql.PlainVanillaPayoff(option_type, strike_price)
        (yyyy,mm,dd) = maturity_yyyy_mm_dd
        maturity_date = ql.Date(dd, mm, yyyy)
        settlement_date = self._calendar.advance(maturity_date, 0, ql.Days)
        exercise = ql.AmericanExercise(settlement_date, maturity_date)
        option = ql.VanillaOption(payoff, exercise)
        return option

    def _create_ts_handles(self, calculation_yyyy_mm_dd, risk_free_rate, dividend_rate, volatility):
        (yyyy,mm,dd) = calculation_yyyy_mm_dd
        calculation_date = ql.Date(dd, mm, yyyy)

        flat_ts = ql.YieldTermStructureHandle(
            ql.FlatForward(calculation_date, risk_free_rate, self._day_count)
        )
        dividend_yield = ql.YieldTermStructureHandle(
            ql.FlatForward(calculation_date, dividend_rate, self._day_count)
        )
        flat_vol_ts = ql.BlackVolTermStructureHandle(
            ql.BlackConstantVol(calculation_date, self._calendar, volatility, self._day_count)
        )
        return (flat_ts, dividend_yield, flat_vol_ts)

    def _create_spot_handle(self, spot_price):
        spot_handle = ql.QuoteHandle(
            ql.SimpleQuote(spot_price)
        )
        return spot_handle

    def price(self, spot_price, strike_price, risk_free_rate, volatility, dividend_rate, maturity_yyyy_mm_dd, calculation_yyyy_mm_dd):

        self._set_calculation_date(calculation_yyyy_mm_dd)

        option = self._create_option(self._option_type, strike_price, maturity_yyyy_mm_dd)
        (flat_ts, dividend_yield, flat_vol_ts) = self._create_ts_handles(calculation_yyyy_mm_dd, risk_free_rate, dividend_rate, volatility)
        spot_handle = self._create_spot_handle(spot_price)

        bsm_process = ql.BlackScholesMertonProcess(spot_handle, 
                                                   dividend_yield, 
                                                   flat_ts, 
                                                   flat_vol_ts)
        time_steps = 100
        option.setPricingEngine(ql.BinomialVanillaEngine(bsm_process,'crr',time_steps))

        bs_price = option.NPV()
        return bs_price
