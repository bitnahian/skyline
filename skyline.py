def merge_outlines(left_outline, right_outline):
    size_left = len(left_outline)
    size_right = len(right_outline)

    # Recreate the merge step in your merge sort
    i, j, h1, h2 = 0, 0, 0, 0 # h1 -> last_seen height of left outline and h2 -> last seen of right
    while(i < size_left and j < size_right):
        to_merge = [0,0]
        left = left_outline[i]
        right = right_outline[j]

        if left[0] < right[0]:
            # If the x-coordinate of the left outline is smaller
            # Add that outline to the solution
            to_merge[0] = left[0]
            to_merge[1] = left[1]

            if(left[1] < h2):
                # If the height that we selected is smaller than the previous height of the other outline
                to_merge[1] = h2
            h2 = right[1] # Update the last-seen height of right outline
            i+=1 # Update pointer to left-outline as it has been added
        elif right[0] < left[0]:
            # If the x-coordinate of the right outline is smaller
            # Add that outline to the solution
            to_merge[0] = right[0]
            to_merge[1] = right[1]

            if(right[1] < h1):
                # If the height of the outline we addded is smaller than the last seen height of the other outline
                to_merge[1] = h2
            h1 = left[1] # Updae the last-seen height of the left outline
            j+=1
        else:
            # Corner case when both the x-coordinates of left and right are the same
            # Choose the point with the greater height
            to_merge[0] = left[0]
            to_merge[1] = max(left[1], right[1])

            # Update last seen height for both
            h1, h2 = left[1], right[1]
            i += 1
            j += 1

        # end of while loop

def getOutline(left, right, tuples):
    if left > right:
        return [] # Return an empty list if called stupidly
    elif left == right:
        # Base case when there is only one student
        x1 = tuples[left][0]
        x2 = tuples[left][1]
        h = tuples[left][2]
        # This is where you add the max height with x1 and 0 with x2
        return [[x1, h], [x2, 0]]
    else:
        # General case where you recurse
        middle = int((left+right)/2)
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
solution = [ (1,3), (3, 7) ]

# output one line for each point (x,y) in the solution
# (your program should not output any other text)
for point in solution:
	x = point[0]
	y = point[1]
	print("{} {}".format(x, y))
