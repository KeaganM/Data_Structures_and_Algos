
def bubble_sort(items:list) -> list:
    n = len(items)
    for i in range(n):
        is_sorted = True
        # allows us to do passes where we start one more element over with each new pass
        for j in range(n-i-1):
            # check to see if the next item is less than current
            if items[j] > items[j+1]:
                # if so swtich them and set sort to false
                items[j],items[j+1] = items[j+1],items[j]
                is_sorted = False
        if is_sorted:
            break
    return items


if __name__ == '__main__':

    a = [8,7,2,3,6,1,0,0,0]
    b = bubble_sort(a)
    print(b)



    quit()