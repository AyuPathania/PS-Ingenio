import re
call_rate= "$00.99"
your_rate = float(call_rate.replace("$", ""))
print(your_rate)  # Output: 0.99

# time duration
time_str = "00:06:00"
# Split into hours, minutes, and seconds
h, m, s = map(int, time_str.split(":"))
# Convert to total seconds
total_seconds_digit = h * 3600 + m * 60 + s
# Assert to validate the conversion
print(total_seconds_digit)


subtotal_cost = "$5.94"
total = total_seconds_digit * your_rate / 60
total_cost = "{:.2f}".format(int(total * 100) / 100)
print(f"Calculated total_cost: {total_cost}")

final_pay = "$2.96"
changed_value= float(total_cost)
discounted_pay = "{:.2f}".format(changed_value * 0.5)
print(f"Calculated discount_cost: {discounted_pay}")

# add "$" sign in 30.00
add_doller_sign_after_discount=f"${discounted_pay}"
print(add_doller_sign_after_discount)


# add "$" sign in 30.00
add_doller_sign_before_discount=f"${total_cost}"
print(add_doller_sign_before_discount)
assert subtotal_cost == add_doller_sign_before_discount, f"Expected {subtotal_cost} but got {add_doller_sign_before_discount}"
assert final_pay == add_doller_sign_after_discount, f"Expected {final_pay} but got {add_doller_sign_after_discount}"


