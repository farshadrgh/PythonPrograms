def smallest_num_in_list(List):
    Min = List[0]
    for a in List:
        if a < Min:
            Min = a
    return Min
print(smallest_num_in_list([5, 2, -10, 0, 20, 100]))
