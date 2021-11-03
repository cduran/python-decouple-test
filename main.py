from decouple import config

test_value = config('TEST')
print(test_value)

new_value = config('NEW_ENV_VAR')
print(new_value)

test_value2 = config('TEST2')
print(test_value2)

new_value2 = config('NEW_ENV_VAR2')
print(new_value2)

new_value3 = config('LAST_LINE')
print(new_value3)


