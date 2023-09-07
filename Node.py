# Vlad Chevdar | CS302 | Aug 25
# Purpose of this file is to have a tree node with user data
from User import *

class Node:
    def __init__(self, user):
        self.__user = user
        self.__height = 1
        self.__left = None
        self.__right = None

    def __del__(self):
        self.__user = None
        self.__height = 0
        self.__left = None
        self.__right = None

    # Return height
    def getHeight(self):
        return self.__height

    # Change height
    def setHeight(self, height):
        self.__height = height

    # Change user
    def setUser(self, user):
        self.__user = user

    # Return user
    def getUser(self):
        return self.__user

    # Return left child
    def getLeft(self):
        return self.__left

    # Return right child
    def getRight(self):
        return self.__right

    # Change right child
    def setRight(self, user_node):
        self.__right = user_node

    # Change left child
    def setLeft(self, user_node):
        self.__left = user_node


