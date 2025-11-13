class NonReq:
    def __init__(self, root:int, height:int):
        self.root = root
        self.height = height
        self.pr = self.__Tree__()

    @staticmethod
    def leftleaf(root:int)->int:
        return (root-4)**2
    @staticmethod
    def rightleaf(root:int)->int:
        return (root+3)*2

    def __Tree__(self, ll=leftleaf, rl=rightleaf) -> dict:
        tr = {1:[self.root]}
        for i in range(2, self.height + 1):
            lvl = []
            for r in tr[i-1]:
                lvl.append(ll(r))
                lvl.append(rl(r))
            tr[i] = lvl
        return tr

    def output(self)->None:
        for i in range(1, self.height + 1):
            print(self.pr[i])

tree = NonReq(int(input("root:")), int(input("height:")))
tree.output()