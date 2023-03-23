def study_schedule(permanence_period, target_time):
    counter = 0

    for i in permanence_period:
        if type(i[0]) != int or type(i[1]) != int or type(target_time) != int:
            return None
        if target_time in range(i[0], i[1] + 1):
            counter += 1
    return counter
