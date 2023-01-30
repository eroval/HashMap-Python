class Hashmap:
    def __init__(self):
        self.limit_size = 2**64
        self.buckets = [None] * 8
        self.curr_size = 0

    def __increasseifneccessary__(self):
        if len(self.buckets)<self.limit_size and (self.curr_size<=len(self.buckets)//1.4925):
            self.buckets.extend([None]*len(self.buckets))

    def __getbucket__(self, key):
        index = self.__getindex__(key)
        return self.buckets[index]

    def __getindex__(self, key):
        return hash(key)%len(self.buckets)

    def __getitem__(self, key):
        bucket = self.__getbucket__(key)
        for i in range(len(bucket)):
            if bucket[i][0]==key:
                return bucket[i][1]
        raise KeyError("No such key")

    def __setitem__(self, key, value):
        index = self.__getindex__(key)
        if(self.curr_size<self.limit_size):
            for i in range(0,3):
                if self.buckets[index] is None:
                    self.buckets[index] = []
                    break
                else:
                    self.__increasseifneccessary__()
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0]==key:
                bucket[i][1]=value
                return None
        
        self.buckets[index].insert(0, [key,value])
        self.curr_size+=1

    def __delitem__(self, key):
        bucket = self.__getbucket__(key)
        for i in range(len(bucket)):
            if bucket[i][0]==key:
                return bucket[i][1]
        raise KeyError("No such key")

    def __str__(self):
        object = "{"
        add_comma = False

        for i in range(0, len(self.buckets)):
            if self.buckets[i] and len(self.buckets[i])>0:
                for j in range(0,len(self.buckets[i])):
                    object+=(
                        ", "+self.__add_quotes__(self.buckets[i][j][0], self.buckets[i][j][1]) if add_comma
                        else self.__add_quotes__(self.buckets[i][j][0], self.buckets[i][j][1])
                    )
                    add_comma=True

        object+="}"
        return object

    def __add_quotes__(self, key, value):
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


if __name__ == "__main__":
    dict
    my_map = Hashmap()
    my_map["cool"]=Hashmap()
    my_map["cool"]["notcool"]=[]
    my_map["cool"]["notcool"].insert(0,1)
    my_map["cool"]["notcool"].insert(0,2)
    my_map["cool"]["notcool"].insert(0,3)
    my_map["2"]="3434"
    # del my_map["cool"]
    print(my_map)
    # coolest = {
    #     "not that cool": 4,
    #     "super cool":5,
    #     "nEsdgsd":5
    # }
    # print(coolest)
