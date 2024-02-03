#Author: @CodeWithSalman
# =========================  PROJECT OVERVIEW. ========================= #
# AVL Tree is self balancing tree. It is similar to binary tree,
# but it is used when do u want to get more accurate and quick results.
# ============= USE OF CLASSES AND FUNCTIONS. =============== #
# DECLARING Node CLASS.
class Node:
    # USE OF CONSTRUCTOR.
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
# NOW DECLARING AVL TREE CLASS.
class AVL_Tree:
    # AGAIN USE OF CONSTRUCTOR.
    def __init__(self):
        self.root = None
    # HEIGHT FUNCTION.
    def height(self, node):
        if not node:
            return 0
        return node.height
    # USE OF UPDATE HEIGHT FUNCTION [LEFT AND RIGHT TREE HEIGHT AS WELL].
    def update_Height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.height(node.left), self.height(node.right))
    # FUNCTION TO MAKE TREE A BALANCED TREE.
    def balance_Factor(self, node):
        if not node:
            return 0
        # BALANCE TREE OR AVL TREE CAN HAVE MAXIMUM HEIGHT 0, 1, -1.
        # SO, IT IS THE FORMULA TO MAKE SURE THE HEIGHT.
        return self.height(node.left) - self.height(node.right)
    # ROTATING TOWARDS LEFT IF HEIGHT OF TREE IS GREATER THAN LIMIT.
    def rotate_Left(self, y):
        # MOVING TOWARDS RIGHT SIDE TREE.
        moving = y.right
        # NOW ROTATING TOWARDS LEFT.
        rotation = moving.left
        moving.left = y
        y.right = rotation
        self.update_Height(y)
        self.update_Height(moving)
        return moving
    # ROTATING TOWARDS RIGHT IF HEIGHT OF TREE IS GREATER THAN LIMIT.
    def rotate_Right(self, x):
        # MOVING TOWARDS LEFT SIDE OF TREE.
        moving = x.left
        # NOW ROTATING TOWARDS RIGHT SIDE.
        rotation = y.right
        y.right = moving
        x.left = rotation
        self.update_Height(x)
        self.update_Height(moving)
        return moving
    # USE OF INSERT FUNCTION.
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root
        self.update_Height(root)
        balance = self.balance_Factor(root)
        # LEFT LEFT ROTATION.
        if balance > 1 and key < root.left.key:
            return self.rotate_Right(root)
        # RIGHT RIGHT ROTATION.
        if balance < -1 and key > root.right.key:
            return self.rotate_Left(root)
        # LEFT TO RIGHT ROTATION.
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_Left(root.left)
            return self.rotate_Right(root)
        # RIGHT TO LEFT ROTATION.
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_Right(root.right)
            return self.rotate_Left(root)
        return root
    # NOW INSERTING KEY USING BELOW FUNCTION.
    def insert_Key(self, key):
        self.root = self.insert(self.root, key)
    # USE OF INORDER FUNCTION.
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
    # USE OF PREORDER FUNCTION.
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    # USE OF POSTORDER FUNCTION.
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")
    # DISPLAY FUNCTION TO SHOW TO ALL THE STRUCTURE OF THE TREE.
    def display(self):
        print("Inorder: ", end=" ")
        self.inorder(self.root)
        print("\nPreorder: ", end=" ")
        self.preorder(self.root)
        print("\nPostorder: ", end=" ")
        self.postorder(self.root)
    # SEARCH FUNCTION TO SEARCH FOR A VALUE.
    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
    # FUNCTION TO FIND MINIMUM VALUE IN THE TREE.
    def minimum_Value(self, root):
        while root.left:
            root = root.left
        return root
    def finding_Min(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root.key
    def finding_Max(self, root):
        if not root:
            return None
        while root.right:
            root = root.right
        return root.key
    # DELETE FUNCTION TO DELETE VALUE.
    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.minimum_Value(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        self.update_Height(root)
        balance = self.balance_Factor(root)
        # LEFT LEFT CASE.
        if balance > 1 and self.balance_Factor(root.left) >= 0:
            return self.rotate_Right(root)
        # RIGHT RIGHT CASE.
        if balance < -1 and self.balance_Factor(root.right) <= 0:
            return self.rotate_Left(root)
        # LEFT TO RIGHT CASE.
        if balance > 1 and self.balance_Factor(root.left) < 0:
            root.left = self.rotate_Left(root.left)
            return self.rotate_Right(root)
        # RIGHT TO LEFT CASE.
        if balance < -1 and self.balance_Factor(root.right) > 0:
            root.right = self.rotate_Right(root.right)
            return self.rotate_Left(root)
        return root
    # FUNCTION TO UPDATE VALUE.
    def update(self, key, new_Key):
        self.root = self.delete(self.root, key)
        self.insert_Key(new_Key)
# MAIN CODE OR DRIVER CODE.
if __name__ == '__main__':
    # CREATING OBJECT OF AVL_Tree Class.
    obj = AVL_Tree()
    while True:
        print("\n1 = Insert Key")
        print("2 = Display Inorder Tree")
        print("3 = Display Preorder Tree")
        print("4 = Display Postorder Tree")
        print("5 = Display Tree")
        print("6 = Search Data")
        print("7 = Delete Data")
        print("8 = Update Data")
        print("9 = Print Minimum Value")
        print("10 = Print Maximum Value")
        print("11 = Exit")
        selection = int(input("Make any One selection from Above: "))
        if selection == 1:
            key = int(input("Enter the Key Value: "))
            obj.insert_Key(key)
        elif selection == 2:
            print("Inorder Tree: ", end=" ")
            obj.inorder(obj.root)
        elif selection == 3:
            print("Preorder: ", end=" ")
            obj.preorder(obj.root)
        elif selection == 4:
            print("Postorder: ", end=" ")
            obj.postorder(obj.root)
        elif selection == 5:
            obj.display()
        elif selection == 6:
            print("\nInorder: ", end=" ")
            obj.inorder(obj.root)
            search_Value = int(input("\nEnter the Value to get Status: "))
            result = obj.search(obj.root, search_Value)
            if result:
                print("Found")
            else:
                print("Not Found")
        elif selection == 7:
            print("\nInorder: ", end=" ")
            obj.inorder(obj.root)
            deleted_Value = int(input("\nEnter the Value to Delete: "))
            result = obj.delete(obj.root, deleted_Value)
        elif selection == 8:
            print("\nInorder: ", end=" ")
            obj.inorder(obj.root)
            old_Value = int(input("Enter the Old Value: "))
            new_Value = int(input("Enter the New Value: "))
            obj.update(old_Value, new_Value)
        elif selection == 9:
            min_Value = obj.finding_Min(obj.root)
            print("The Minimum Value is: ", min_Value)
        elif selection == 10:
            max_Value = obj.finding_Max(obj.root)
            print("The Maximum Value is: ", max_Value)
        elif selection == 11:
            exit()
        else:
            print("Input Out of Range OR Invalid Input.")
