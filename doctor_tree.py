class DoctorNode:
    """
    Represents a doctor in the reporting structure.
    Each doctor can have up to two direct reports.
    """

    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """
    Manages the doctor reporting hierarchy using a binary tree.
    """

    def __init__(self):
        self.root = None

    def insert(
        self, parent_name: str, doctor_name: str, side: str, current_node=None
    ) -> bool:
        side = side.strip().lower()
        parent_name = parent_name.strip()
        doctor_name = doctor_name.strip()

        if side not in ["left", "right"]:
            print("Invalid side, use left or right.")
            return False

        if self.root is None:
            print("No root doctor exists yet.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name.lower() == parent_name.lower():
            if side == "left":
                if current_node.left is None:
                    current_node.left = DoctorNode(doctor_name)
                    return True
                print("Left side already occupied.")
                return False

            if side == "right":
                if current_node.right is None:
                    current_node.right = DoctorNode(doctor_name)
                    return True
                print("Right side already occupied.")
                return False

        if current_node.left:
            if self.insert(parent_name, doctor_name, side, current_node.left):
                return True

        if current_node.right:
            if self.insert(parent_name, doctor_name, side, current_node.right):
                return True

        if current_node == self.root:
            print(f"Parent doctor '{parent_name}' not found.")
        return False

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder Traversal:")
    print(tree.preorder(tree.root))

    print("\nInorder Traversal:")
    print(tree.inorder(tree.root))

    print("\nPostorder Traversal:")
    print(tree.postorder(tree.root))
