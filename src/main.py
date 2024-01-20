from utilts import *

executed = operations_get_executed(json_load())
operations = operations_sort_date(executed)
dates = date_change(operations)
card_number = mask_card_number(operations)
amount_number = mask_amount_number(operations)

for operation in range(len(operations)):
    print(f"{dates[operation]} {operations[operation]['description']}")
    print(f"{card_number[operation]} -> Счет {amount_number[operation]}")
    print(f"{operations[operation]['operationAmount']['amount']} {operations[operation]['operationAmount']['currency']['name']}\n")
