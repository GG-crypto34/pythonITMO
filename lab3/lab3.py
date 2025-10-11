class BinTree:
    """Class that constructs a binary tree from start value and height
    :param root: start value
    :param height: height of binary tree
    """
    def __init__(self,root:int,height:int):
        self.root = root
        self.height = height
        self.T = self.__getBinTree__(self.root,self.height)

    def __getBinTree__(self,root:int,height:int):
        """Private recursive function that builds a binary tree from given height and start value, using functions BinTree.left() and BinTree.right()
        :param root: The root of the binary tree
        :param height: The height of the binary tree
        """
        if height > 1:	return {root:[self.__getBinTree__(self.left(root),height-1), self.__getBinTree__(self.right(root),height-1)]}
        elif height == 1: return {root:"end"}
        return {}
    @staticmethod
    def left(root:int)->int:
        """Function that returns the left child of the binary tree
        :param root: The root of the left child of the binary tree"""
        return root**2
    @staticmethod
    def right(root:int)->int:
        """Function that returns the right child of the binary tree
        :param root: The root of the right child of the binary tree"""
        return root-2
    @staticmethod
    def __pars__(data0, height0:int)->dict:
        """Private function that rebuilds the binary tree in dictionary form
        :param data0: The binary tree({"root":[{leftLeaf},{rightLeaf}]})
        :param height0: The height of the binary tree
        :return: The rebuilt binary tree in dictionary form"""
        dict1 = {}
        for height in range(1, height0 + 1):
            dict1[height] = ""
        def pars1(data, height1):
            """"In-Built function that rebuilds the binary tree in dictionary form"""
            if isinstance(data, dict):
                for key, value in data.items():
                    dict1[height1] += " " + str(key)
                    pars1(value, height1 - 1)
            elif isinstance(data, list):
                for value in data:
                    pars1(value, height1 - 1)
        pars1(data0, height0)
        return dict1

    def output(self)->None:
        """Function that prints the binary tree in readable format from BinTree.__pars__() output
        :return: None"""
        dict1 = self.__pars__(self.T, self.height*2)
        for height in range(int(len(dict1.keys()))):
            print(dict1[int(len(dict1.keys())) - height])
#rtp = {"1":[{"2L":[{"3LL":""},{"3LR":""}]},{"2R":[{"3RL":""},{"3RR":""}]}]}

tree = BinTree(5,6)
print(help(BinTree))
tree.output()
