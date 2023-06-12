# 1.3 Write a program to check two strings are equal or not.

class Task3:

    def task3(self, s1, s2):
        if str(s1) == str(s2):
            return "string1 is : {} | string2 is : {} are equal".format(s1, s2)
        else:
            return "string1 is : {} | string2 is : {} are not equal".format(s1, s2)


if __name__ == "__main__":
    obj = Task3()
    # s1 = input("Enter string1 is: ")
    s1 = "vijaya"
    # s2 = input("Enter string2 is: ")
    s2 = "vijaya"
    print(obj.task3(s1, s2))
