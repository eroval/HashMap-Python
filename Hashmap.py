class Hashmap:
    def __init__(self):
        self.limit_size = 2**64
        self.buckets = [None] * 8
        self.curr_size = 0
        self.ratio_resizer = 1.4925
        self.upper_threshold = len(self.buckets)//self.ratio_resizer
        self.lower_threshold = len(self.buckets)//2//self.ratio_resizer

    def __increase_if_neccessary__(self):
        if len(self.buckets)<self.limit_size and (self.curr_size>=self.upper_threshold):
            self.__rehash__()

    def __decrease_if_neccessary__(self):
        if len(self.buckets)>8 and self.curr_size<=self.lower_threshold:
            self.__rehash__(False)

    def __recalculate__ratio__(self, size):
        self.upper_threshold = size//self.ratio_resizer
        self.lower_threshold = size//2//self.ratio_resizer

    def __rehash__(self, increase=True):
        if increase:
            new_buckets = [None]*(len(self.buckets)*2)
            self.__recalculate__ratio__(len(new_buckets))
        else:
            new_buckets = [None]*(len(self.buckets)//2)
            self.__recalculate__ratio__(len(new_buckets))

        for bucket_idx in range(0, len(self.buckets)):
            if self.buckets[bucket_idx]:
                for item_idx in range(0, len(self.buckets[bucket_idx])):
                    new_index = self.__caluclate_new_index__(self.buckets[bucket_idx][item_idx][0], new_buckets)

                    if new_buckets[new_index] is None:
                        new_buckets[new_index] = []

                    new_buckets[new_index].insert(0,self.buckets[bucket_idx][item_idx])
    
        self.buckets = new_buckets

    def __getbucket__(self, key):
        index = self.__getindex__(key)
        return self.buckets[index]

    def __getindex__(self, key):
        return hash(key)%len(self.buckets)

    def __caluclate_new_index__(self, key, new_buckets):
        return hash(key)%len(new_buckets)

    def __getitem__(self, key):
        index = self.__getindex__(key)
        if self.buckets[index]:
            for i in range(len(self.buckets[index])):
                if self.buckets[index][i][0]==key:
                    return self.buckets[index][i][1]

        raise KeyError("No such key")

    def __setitem__(self, key, value):
        index = self.__getindex__(key)

        if self.buckets[index] is None:
            self.buckets[index] = []
                    
        for i in range(len(self.buckets[index])):
            if self.buckets[index][i][0]==key:
                self.buckets[index][i][1]=value
                return None

        self.buckets[index].insert(0, [key,value])
        self.curr_size+=1
        self.__increase_if_neccessary__()
       
    def __delitem__(self, key):
        index = self.__getindex__(key)
        
        for i in range(len(self.buckets[index])):
            if self.buckets[index][i][0]==key:
                value = self.buckets[index].pop(i)
                self.curr_size-=1
                self.__decrease_if_neccessary__()
                return value
        raise KeyError("No such key")
        
    def __str__(self):
        object = "{"
        add_comma = False

        for i in range(0, len(self.buckets)):
            if self.buckets[i] and len(self.buckets[i])>0:
                for j in range(0,len(self.buckets[i])):
                    object+=(
                        ", "+self.__addquotes__(self.buckets[i][j][0], self.buckets[i][j][1]) if add_comma
                        else self.__addquotes__(self.buckets[i][j][0], self.buckets[i][j][1])
                    )
                    add_comma=True

        object+="}"
        return object

    def __addquotes__(self, key, value):
        modified_string=""

        # add if necessary for key 
        if(type(key)==str):
            modified_string+=f"\'{(key)}\': "
        else:
            modified_string+=f"{(key)}: "

        # add if necessary for value
        if(type(value)==str):
            modified_string+=f"\'{(value)}\'"
        else:
            modified_string+=f"{(value)}"

        return modified_string


def test_1():
    my_map = Hashmap()
    my_map["cool"]=Hashmap()
    my_map["cool"]["notcool"]=[]
    my_map["cool1"]=1
    my_map["cool2"]=2
    my_map["cool3"]=3
    my_map["cool4"]=4
    my_map["cool5"]=5
    my_map["cool"]["notcool"].insert(0,1)
    my_map["cool"]["notcool"].insert(0,2)
    my_map["cool"]["notcool"].insert(0,3)
    print(my_map)
    del my_map["cool"]["notcool"]
    print(my_map)
    del my_map["cool2"]
    print(my_map)

def test_2():
    my_map = Hashmap()
    for i in range (0, 1043):
        key = f"cool{i}"
        value = f"not that cool {i}"
        my_map[key]=value
    print(my_map)


if __name__ == "__main__":
    test_1()
    # test_2()
