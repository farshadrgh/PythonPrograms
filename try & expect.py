try:
    result = []
    for i in range(0,11):
        result.append(i)
except:

    print("Something is wrong!!!")
finally:

    print("Our result is: {}".format(result))