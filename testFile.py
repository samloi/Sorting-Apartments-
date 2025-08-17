from Apartment import Apartment
from lab06 import merge_sort, ensure_sorted_ascending, get_best_apartment, get_worst_apartment, get_affordable_apartments


#Apartment Class 
def test_apartment_class():
    apartment = Apartment(1300, 250, "average")
    assert apartment.get_rent() == 1300
    assert apartment.get_meters_from_UCSB() == 250
    assert apartment.get_condition() == "average"
    assert apartment.get_apartment_details() == "(Apartment) Rent: $1300, Distance From UCSB: 250m, Condition: average"

def test_overload(): 
    apartment1 = Apartment(950, 215, "excellent")
    apartment2 = Apartment(950, 190, "excellent")
    assert apartment1 > apartment2
    assert apartment2 < apartment1
    apartment3 = Apartment(950, 215, "excellent")
    assert apartment1 == apartment3

def test_equality(): 
    apartment1 = Apartment(1600, 299, "excellent")
    apartment2 = Apartment (1600, 299, "excellent")
    apartment3 = Apartment (1600, 299, "average")
    apartment4 = Apartment (1100, 299, "excellent")
    apartment5 = Apartment (1600, 199, "excellent")
    assert apartment1 == apartment2
    assert apartment1 != apartment3
    assert apartment1 != apartment4
    assert apartment1 != apartment5

#LAB06.PY 
def test_merge_sort(): 
    apartment0 = Apartment(1116, 216, "bad")
    apartment1 = Apartment(949, 216, "average")
    apartment2 = Apartment(949, 216, "excellent")
    apartment3 = Apartment(949, 191, "excellent")
    apartment4 = Apartment(900, 191, "excellent")
    apartment5 = Apartment(550, 249, "bad")
    apartmentList = [apartment0, apartment1, apartment2, apartment3, apartment4, apartment5]
    sort_list = merge_sort(apartmentList)
    assert ensure_sorted_ascending(sort_list)
    assert sort_list == [
        apartment5,
        apartment4, 
        apartment3,
        apartment2, 
        apartment1, 
        apartment0

    ]

def test_ensure_sorted_ascending(): 
    apartment0 = Apartment(550, 249, "bad")
    apartment1 = Apartment(900, 191, "excellent")
    apartment2 = Apartment(949, 191, "excellent")
    apartment3 = Apartment(949, 216, "excellent")
    apartment4 = Apartment(949, 216, "average")
    apartment5 = Apartment(1116, 216, "bad")
    apartmentList0 = [apartment0, apartment1, apartment2, apartment3, apartment4, apartment5]
    assert ensure_sorted_ascending(apartmentList0) == True
    apartment6 = Apartment(1000, 199, "average")
    apartmentList1 = [apartment6, apartment1, apartment2]
    assert ensure_sorted_ascending(apartmentList1) == False


def test_get_best_apartment(): 
    apartment0 = Apartment(1300, 199, "average")
    apartment1 = Apartment(1300, 199, "excellent")
    apartment2 = Apartment(1000, 99, "average")
    apartment3 = Apartment(1000, 215, "excellent")
    apartment4 = Apartment(700, 300, "bad")
    apartment5 = Apartment(800, 260, "excellent")
    apartmentList = [apartment0, apartment1, apartment2, apartment3, apartment4, apartment5]
    assert get_best_apartment(apartmentList) == "(Apartment) Rent: $700, Distance From UCSB: 300m, Condition: bad"

def test_get_worst_apartment(): 
    apartment0 = Apartment(1202, 199, "average")
    apartment1 = Apartment (1202, 199, "excellent")
    apartment2 = Apartment (1000, 99, "average")
    apartment3 = Apartment (1000, 216, "excellent")
    apartment4 = Apartment (701, 316, "bad")
    apartment5 = Apartment (801, 251, "excellent")
    apartmentList = [apartment0, apartment1, apartment2, apartment3, apartment4, apartment5]
    assert get_worst_apartment(apartmentList) == "(Apartment) Rent: $1202, Distance From UCSB: 199m, Condition: average"

def test_get_affordable_apartments(): 
    apartment0 = Apartment(1115, 216, "bad")
    apartment1 = Apartment(971, 216, "average")
    apartment2 = Apartment(960, 216, "average")
    apartment3 = Apartment(960, 191, "excellent")
    apartment4 = Apartment(900, 191, "excellent")
    apartment5 = Apartment(500, 251, "bad")
    apartmentList = [apartment0, apartment1, apartment2, apartment3, apartment4, apartment5]
    output = (
        "(Apartment) Rent: $500, Distance From UCSB: 251m, Condition: bad\n"
        "(Apartment) Rent: $900, Distance From UCSB: 191m, Condition: excellent\n"
        "(Apartment) Rent: $960, Distance From UCSB: 191m, Condition: excellent\n"
        "(Apartment) Rent: $960, Distance From UCSB: 216m, Condition: average"
    )
    assert get_affordable_apartments(apartmentList, 960) == output

    




