#!/usr/bin/env python3

def calc_final_ret_amount(invest_each_time, years, annual_ret, interval_cnt_a_year):
    interval_net_value = pow(annual_ret + 1, 1 / interval_cnt_a_year)
    interval_cnt_total = years * interval_cnt_a_year
    final_net_value = \
            (pow(interval_net_value, interval_cnt_total + 1) - 1) / \
            (interval_net_value - 1) - 1
    final_ret_amount = invest_each_time * final_net_value
    return round(final_ret_amount, 2)

print(calc_final_ret_amount(300, 3, 0.1, 12))

