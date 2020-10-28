def my_round(number: float, digits=0):
    if not isinstance(number, float):
        raise ValueError(f'Недопустимый параметр. Ожидалось float, получено: {type(number)}')
    int_part = int(number)
    work_value = number - int_part
    if digits == 0:
        return int_part
    else:
        str = f'{work_value}'
        if len(str) <= digits:
            return number
        else:
            if int(str[digits+1]) >= 5:
                
    return work_value


print(my_round(15.122))

