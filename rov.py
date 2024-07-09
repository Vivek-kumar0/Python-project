def count_substring(string, sub_string):
    a=string.lower()
    b=sub_string.lower()
    c=a.count(b)
    
    return c


print(count_substring('i AM birth','Birth'))
