# Vlad Chevdar | CS302 | Aug 25
# Purpose of this file is to store users in the AVL tree 
from Node import *

class AVL:
    def __init__(self):
        self.__root = None 
    
    def __del__(self):
        self.__root = None

    # Add data from external file to the tree
    def load_data(self, filename):
        with open(filename, 'r') as file:
            file_data = file.read()
            lines = file_data.strip().split('\n')
            for line in lines:
                contents = line.split('|') 
                if len(contents) > 2:
                    first_name = contents[0]
                    last_name = contents[1]
                    password = contents[2]
                    locations = contents[3:-1]
                    existing_user = User(first_name, last_name, password)
                    self.insert(existing_user)

                    for location in locations:
                        existing_user.add_to_history(location)
    
    # Return the number of users in the database
    def count_users(self):
        return self.__count_users(self.__root)

    # count users in the tree
    def __count_users(self, root):
        if not root:
            return 0

        return 1 + self.__count_users(root.getLeft()) + self.__count_users(root.getRight())

    # save data to an external file     
    def save_data(self, filename):
        with open(filename, 'w') as file:
            self.__write_data(self.__root, file)

    # write each user data
    def __write_data(self, root, file):
        if root:
            line = root.getUser().get_data()
            file.write(str(line) + '\n')
            self.__write_data(root.getLeft(), file)
            self.__write_data(root.getRight(), file)

    # Display all users
    def __display(self, root, level):
        if root is None:
            return 0
        root.getUser().display()
        return 1 + self.__display(root.getLeft(), level + 1) + self.__display(root.getRight(), level +1 )

    # Display all users, helper
    def display(self):
        total = self.__display(self.__root, 1)

    # Return the data of the user
    def __get_user(self, root, user):
        if root is None:
            return False

        result = root.getUser().compare(user)
        if result > 0:
            return self.__get_user(root.getLeft(), user)
        elif result < 0:
            return self.__get_user(root.getRight(), user)
        else:
            return root.getUser()

    # Return the user
    def get_user(self, user):
        return self.__get_user(self.__root, user)

    # find user in the tree
    def __find(self, root, user):
        if root is None:
            return False

        result = root.getUser().compare(user)
        if result > 0:
            return self.__find(root.getLeft(), user)
        elif result < 0:
            return self.__find(root.getRight(), user)
        else:
            return True

    # find a user in the tree
    def find(self, user):
        if (user is None):
            raise Exception("User's data is empty!")

        return self.__find(self.__root, user)

    # find user and compare password 
    def __verify(self, root, user):
        if root is None:
            return False

        result = root.getUser().compare(user)
        if result > 0:
            return self.__verify(root.getLeft(), user)
        elif result < 0:
            return self.__verify(root.getRight(), user)
        else:
            return root.getUser().login(user)

    # find the user in the tree and return true if password match
    def verify(self, user):
        if (user is None):
            return False
        return self.__verify(self.__root, user)

    # Right rotation
    def __right_rotate(self, y):
            x = y.getLeft()
            T3 = x.getRight()

            x.setRight(y)
            y.setLeft(T3)

            self.__update_height(y)
            self.__update_height(x)

            return x

    # Left rotation
    def __left_rotate(self, x):
        y = x.getRight()
        T2 = y.getLeft()

        y.setLeft(x)
        x.setRight(T2)

        self.__update_height(x)
        self.__update_height(y)

        return y
    
    # Insert to the AVL Tree, helper
    def insert(self, user):
        self.__root, is_inserted = self.__insert(self.__root, user)
        return is_inserted

    # Insert to the AVL Tree
    def __insert(self, root, user):
        if root is None:
            return Node(user), True

        comparison = root.getUser().compare(user)
        is_inserted = False
        if comparison > 0:
            left_child, is_inserted = self.__insert(root.getLeft(), user)
            root.setLeft(left_child)
        elif comparison < 0:
            right_child, is_inserted = self.__insert(root.getRight(), user)
            root.setRight(right_child)
        else:
            return root, False # Dublicate data

        self.__update_height(root)
        balance = self.__get_balance(root)

        if balance > 1 and user.compare(root.getLeft().getUser()) < 0:
            return self.__right_rotate(root), is_inserted

        if balance < -1 and user.compare(root.getRight().getUser()) > 0:
            return self.__left_rotate(root), is_inserted

        if balance > 1 and user.compare(root.getLeft().getUser()) > 0:
            root.setLeft(self.__left_rotate(root.getLeft()))
            return self.__right_rotate(root), is_inserted

        if balance < -1 and user.compare(root.getRight().getUser()) < 0:
            root.setRight(self.__right_rotate(root.getRight()))
            return self.__left_rotate(root), is_inserted

        return root, is_inserted

    # Return height of the Tree    
    def __get_height(self, root):
        if not root:
            return 0
        return root.getHeight()

    # Update height of each root
    def __update_height(self, root):
        root.setHeight(1 + max(self.__get_height(root.getLeft()), self.__get_height(root.getRight())))

    # Return balance factor of the AVL tree
    def __get_balance(self, root):
        if not root:
            return 0
        return self.__get_height(root.getLeft()) - self.__get_height(root.getRight())