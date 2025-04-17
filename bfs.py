binary_tree = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 4,
            "left": None,
            "right": None
        },
        "right": {
            "value": 5,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 3,
        "left": {
            "value": 6,
            "left": None,
            "right": None
        },
        "right": None
    }
}


def show_tree(node):

    queue = []
    depth = 0
    queue.append((node, depth))
    while len(queue) > 0:
        node, depth = queue.pop()

        # Print the current node's value
        print(node["value"])

        # Add left and right children to the queue if they exist
        if node["left"]:
            queue.append((node["left"], depth + 1))
        if node["right"]:
            queue.append((node["right"], depth + 1))


       




show_tree(binary_tree)