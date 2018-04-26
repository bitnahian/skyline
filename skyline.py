def merge_outlines(left_outline, right_outline):
    merged_outline = []
    size_left = len(left_outline)
    size_right = len(right_outline)

    # Recreate the merge step in your merge sort
    i, j, h1, h2 = 0, 0, 0, 0 # h1 -> last_seen height of left outline and h2 -> last seen of right
    while(i < size_left and j < size_right):
        left = left_outline[i]
        right = right_outline[j]

        if left[0] < right[0]: # If the x-coordinate of the left-outline is more to the left
            x1 = left[0]
            h1 = left[1]

            maxh = max(h1, h2)
            merged_outline.append([x1, maxh])
            i += 1
        elif right[0] < left[0]:
            x2 = right[0]
            h2 = right[1]

            maxh = max(h1, h2)
            merged_outline.append([x2, maxh])
            j+=1
        else:
            h1 = left[1]
            h2 = right[1]

            maxh = max(h1,h2)
            merged_outline.append([left[0], maxh])
            i += 1
            j += 1
        # end of while loop
    while i < size_left:
        # While there are still elements inside the left_outline
        merged_outline.append(left_outline[i])
        i += 1

    while j < size_right:
        # While there are still elements inside the right_outline
        merged_outline.append(right_outline[j])
        j += 1
        # Removal of redundant points from the outline
    curr = 0
    while curr < len(merged_outline):
        duplicate = True
        k = curr + 1
        while (k < len(merged_outline)) and duplicate is True:
            if merged_outline[curr][1] == merged_outline[k][1]:
                merged_outline.pop(k)
                duplicate = True
            else:
                duplicate = False
        curr += 1

    return merged_outline

def getOutline(left, right, tuples):
    if left > right:
        return [] # Return an empty list if called stupidly
    elif left == right:
        # Base case when there is only one student
        x1 = tuples[left][0]
        x2 = tuples[left][1]
        h = tuples[left][2]

        e1 = [x1, h]
        e2 = [x2, 0]
        # This is where you add the max height with x1 and 0 with x2
        m = []
        m.append(e1)
        m.append(e2)
        return m
    else:
        # General case where you recurse
        middle = (left+right)//2
        # Recursively create the right and the left outlines
        left_outline = getOutline(left, middle, tuples)
        right_outline = getOutline(middle+1, right, tuples)
        # Return a merged version of both outlines
        return merge_outlines(left_outline, right_outline)



# read the number of students
n = int(input())

# read the input data into a few lists
# you could use a different structure if you wanted
tuples = []

for _ in range(n):
	left, right, height = map(int, input().strip().split(' '))
	tuples.append((left, right, height))

# TODO: implement your algorithm
solution = getOutline(0, len(tuples)-1, tuples)


# output one line for each point (x,y) in the solution
# (your program should not output any other text)
for point in solution:
	x = point[0]
	y = point[1]
	print("{} {}".format(x, y))
