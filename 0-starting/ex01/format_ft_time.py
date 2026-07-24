import time
import datetime

curr_time = time.time()
t = datetime.datetime.now()
print(f"Seconds since January 1, 1970: {curr_time:,.4f} or {curr_time:.2e} in scientific notation")
# print("Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation")
print(f"{t.strftime("%b")} {t.strftime("%d")} {t.strftime("%Y")}")
# print("Oct 21 2022")
