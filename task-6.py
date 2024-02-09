"""
Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
"""


# Helpers for greedy algorithm method
def calculate_ratio(item):
    return item[1]["calories"] / item[1]["cost"]


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=calculate_ratio, reverse=True)
    selected_items = {}
    remaining_budget = budget

    for item_name, item_data in sorted_items:
        if item_data["cost"] <= remaining_budget:
            quantity = remaining_budget // item_data["cost"]
            selected_items[item_name] = quantity
            remaining_budget -= item_data["cost"] * quantity

    return selected_items


# Helpers for dynamic programmnig method
def calculate_ratios(items):
    return {food: items[food]["calories"] / items[food]["cost"] for food in items}


def sort_items_by_ratio(items, ratios):
    return sorted(items.keys(), key=lambda x: ratios[x], reverse=True)


def initialize_dp_arrays(budget):
    return [0] * (budget + 1), [None] * (budget + 1)


def fill_dp_arrays(items, sorted_items, budget, dp, prev):
    for food in sorted_items:
        cost = items[food]["cost"]
        calories = items[food]["calories"]
        for j in range(cost, budget + 1):
            if dp[j - cost] + calories > dp[j]:
                dp[j] = dp[j - cost] + calories
                prev[j] = food


def reconstruct_result(items, budget, prev):
    result = {}
    current_budget = budget
    while prev[current_budget] is not None:
        food = prev[current_budget]
        result[food] = result.get(food, 0) + 1
        current_budget -= items[food]["cost"]
    return result


def dynamic_programming(items, budget):
    ratios = calculate_ratios(items)
    sorted_items = sort_items_by_ratio(items, ratios)
    dp, prev = initialize_dp_arrays(budget)
    fill_dp_arrays(items, sorted_items, budget, dp, prev)
    result = reconstruct_result(items, budget, prev)
    return result


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    budget = 1220  # change the budget to check the results

    greedy_res = greedy_algorithm(items, budget)
    print(f"Greedy algorithm set: {greedy_res}")

    dp_res = dynamic_programming(items, budget)

    print(f"Dynamic programming set: {dp_res}")
