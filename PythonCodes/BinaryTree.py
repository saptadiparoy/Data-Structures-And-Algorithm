class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    value = input("Enter value (or 'None' for no node): ").strip()
    if value.lower() == 'none' or value == '':
        return None

    node = Node(value)
    print(f"-- Building left child of '{value}' --")
    node.left = build_tree()
    print(f"-- Building right child of '{value}' --")
    node.right = build_tree()
    return node


def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result


def main():
    print("=== Build your binary tree ===")
    print("At each prompt, enter a value, or 'None' to skip that node.\n")

    root = build_tree()

    if root is None:
        print("\nTree is empty. Nothing to traverse.")
        return

    while True:
        print(""" Choose a traversal:
1. Pre-order (Root -> Left -> Right)
2. In-order (Left -> Root -> Right)
3. Post-order (Left -> Right -> Root)
4. Exit
""")

        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            print("Pre-order:", " -> ".join(preorder(root)))
        elif choice == '2':
            print("In-order:", " -> ".join(inorder(root)))
        elif choice == '3':
            print("Post-order:", " -> ".join(postorder(root)))
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
