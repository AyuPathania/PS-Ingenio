# from faker import Faker
# fake = Faker()

# print(fake.credit_card_number(card_type="visa"))
# print(fake.credit_card_expire())
# print(fake.credit_card_security_code(card_type="visa"))
# print(fake.postcode())

# fee = " 00:02:17"
# minutes = int(fee.split(":")[1].strip())

# # Fix: Only set seconds once
# if fee.split(":")[2].strip().startswith("0"):
#     seconds = int(fee.split(":")[2].strip()[-1])  # seconds = 7
# else:
#     seconds = int(fee.split(":")[2].strip())

# total_seconds = (minutes * 60) + seconds
# # print(f"Minutes: {minutes}")
# # print(f"Seconds: {seconds}")
# # print(f"Total seconds: {total_seconds}")
# # print(f"Time: {minutes}:{seconds:02d} = {total_seconds} seconds")
# print(total_seconds)

# paid_seconds = "8"
# expected_total_earned = "0.58"
# expected_connection_fee = "0.04"
# expected_platform_fee = "1.04"      
# total_credit_charged = "1.66"
# your_rate = "12.49"


# total = float(paid_seconds)*float(your_rate)/60
# total_cost = "{:.2f}".format(int(total * 100) / 100)
# # print(f"Truncated result: {total_cost}")

# connection = (0.36/60)*float(paid_seconds)
# connection_fee = "{:.2f}".format(int(connection * 100) / 100)
# # print(f"connection_fee: {connection_fee}")

# # Fix: Use the numeric value, not the formatted string
# total = (((float(your_rate)/60)*float(paid_seconds)) - (float(connection * 100) / 100))*0.36
# total_earned = "{:.2f}".format(int(total * 100) / 100)
# # print(f"total_earned: {total_earned}")



# # Calculate platform fee: (total_cost - connection_fee) - total_earned
# platform_fee_calc = (float(total_cost) - float(connection_fee)) - float(total_earned)
# platform_fee = "{:.2f}".format(int(platform_fee_calc * 100) / 100)
# # print(f"platform_fee: {platform_fee}")

# # Fix syntax error and convert strings to floats for comparison
# # assert float(total_cost) == total_credit_charged
# # assert float(connection_fee) == expected_connection_fee
# # assert float(total_earned) == expected_total_earned
# # assert float(platform_fee) == expected_platform_fee

# try:
#     assert float(total_cost) == float (total_credit_charged)
# except AssertionError:
#     print(f"Assertion failed for total_cost: expected {total_credit_charged}, found {total_cost}")
#     raise

# try:
#     assert float(connection_fee) == float (expected_connection_fee)
# except AssertionError:
#     print(f"Assertion failed for connection_fee: expected {expected_connection_fee}, found {connection_fee}")
#     raise

# try:
#     assert float(total_earned) == float (expected_total_earned)
# except AssertionError:
#     print(f"Assertion failed for total_earned: expected {expected_total_earned}, found {total_earned}")
#     raise

# try:
#     assert float(platform_fee) == float (expected_platform_fee)
# except AssertionError:
#     print(f"Assertion failed for platform_fee: expected {expected_platform_fee}, found {platform_fee}")
#     raise

# print("✅ All assertions passed!")

pay_button="$1.00"
actual_amount="$1.00"

pay_button_text= f'Pay ('+pay_button+')'
pay_button_verify_text= f'Pay ('+actual_amount+')' 
print(pay_button_text)
print(pay_button_verify_text)












