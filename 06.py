from Apartment import Apartment 


def merge_sort(apartmentList):
    if len(apartmentList) <= 1:
        return apartmentList
    
    midpoint = len(apartmentList) // 2
    left_segment = apartmentList[:midpoint]
    right_segment = apartmentList[midpoint:]

    sorted_left_segment = merge_sort(left_segment)
    sorted_right_segment = merge_sort(right_segment)

    result_list = []
    left_pos = 0
    right_pos = 0

    while left_pos < len(sorted_left_segment) and right_pos < len(sorted_right_segment):
        left_apartment = sorted_left_segment[left_pos]
        right_apartment = sorted_right_segment[right_pos]

        if left_apartment < right_apartment:
            result_list.append(left_apartment)
            left_pos += 1
        else:
            result_list.append(right_apartment)
            right_pos += 1

    while left_pos < len(sorted_left_segment):
        left_apartment = sorted_left_segment[left_pos]
        result_list.append(left_apartment)
        left_pos += 1

    while right_pos < len(sorted_right_segment):
        right_apartment = sorted_right_segment[right_pos]
        result_list.append(right_apartment)
        right_pos += 1

    # Update the original list
    for i in range(len(apartmentList)):
        apartmentList[i] = result_list[i]

    return apartmentList


def ensure_sorted_ascending(apartmentList):
    for i in range(len(apartmentList) - 1):
        present_apartment = apartmentList[i]
        next_apartment = apartmentList[i + 1]
        if present_apartment > next_apartment:
            return False
    return True

def get_best_apartment(apartmentList):
    sorted_apartment_list = merge_sort(apartmentList)
    best_apartment = sorted_apartment_list[0]
    best_apartment_details = best_apartment.get_apartment_details()

    return best_apartment_details

def get_worst_apartment(apartmentList):
    sorted_apartment_list = merge_sort(apartmentList)
    worst_apartment = sorted_apartment_list[-1]
    worst_apartment_details = worst_apartment.get_apartment_details()
    return worst_apartment_details

def get_affordable_apartments(apartmentList, budget):
    sorted_apartment_list = merge_sort(apartmentList)
    affordable_apartments = []

    for apartment in sorted_apartment_list:
        if apartment.get_rent() <= budget:
            affordable_apartments.append(apartment)

    affordable_apartment_details = []

    for apartment in affordable_apartments:
        details = apartment.get_apartment_details()
        affordable_apartment_details.append(details)

    result_string = ""

    for i in range(len(affordable_apartment_details)):
        result_string += affordable_apartment_details[i]
        if i < len(affordable_apartment_details) - 1:
            result_string += "\n"

    return result_string