import heapq

def min_cost_of_connection(cables):

    # Ініціалізуємо мінімальну купу з початковими довжинами кабелів
    heapq.heapify(cables)

    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:

        # Витягуємо два найкоротші кабелі
        first_shortest = heapq.heappop(cables)
        second_shortest = heapq.heappop(cables)
        
        # Витрати на з'єднання двох кабелів
        cost = first_shortest + second_shortest
        total_cost += cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [10, 23, 74, 5, 46, 35, 21, 64]
print("Мінімальні загальні витрати:", min_cost_of_connection(cables))
