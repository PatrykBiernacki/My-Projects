"""Converts roman number to arabic. Two methods available. One using lists second using generator. Decorator measures execution time."""

import time

class ExecTime:
    """Measures time it took to execute task."""

    def __init__(self, funct:callable) -> None:
        self.funct = funct


    def __call__(self, *args, **kwargs) -> None:
        """Measures execution time of decorated function."""
        time_start = time.perf_counter()
        wrapped_funct = self.funct(self, *args, **kwargs)
        time_end = time.perf_counter()
        print(f'Method: {self.funct.__name__}. Exec time: {time_end-time_start}')
        return wrapped_funct

class RomanToInt:
    
    @ExecTime
    def roman_to_int_list(self, roman_number:str) ->int:
        roman_list = []
        roman_list[:0] = roman_number
        roman_nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        converted_number = 0
        
        for index_no, roman_num in enumerate(roman_list):
            roman_list[index_no] = roman_nums[roman_num]
        
        for index_no, value in enumerate(roman_list[:-1]):
            if value >= roman_list[index_no+1]:
                converted_number += value
            else:    
                converted_number -= value
            
        converted_number += roman_list[-1]   
            
        return converted_number

    @ExecTime
    def roman_to_int_gen(self, roman_number:str) ->int:
        
        roman_gen = (x for x in roman_number)

        roman_nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}     
        converted_number = 0
        
        prev_item = next(roman_gen)

        converted_number = 0
        for item in roman_gen:    
    
            if roman_nums[prev_item] >= roman_nums[item]:
                converted_number += roman_nums[prev_item]
                prev_item = item
            else:    
                converted_number -= roman_nums[prev_item]
                prev_item = item
   
        converted_number += roman_nums[prev_item]
            
        return converted_number
 
def main():
    roman = RomanToInt()
    
    numbers_roman = ("III", "LVIII", "MCMXCIV")
    for number in numbers_roman:
        print(roman.roman_to_int_list(number)) 
        print(roman.roman_to_int_gen(number)) 
    
    
if __name__ == '__main__':
    main()    