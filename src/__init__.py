import pandas as pd;
import numpy as np;
class DataPrepKit:
    __path =""
    __extantion =""
    __extantions = ["csv","json","xlsx"]
    __args = None
    __data = None
    def __init__(self,path,**args):
        self.__path = path    
        self.__args = args
        lst = path.split(".")
        self.__extantion = lst[-1]
        if(self.__extantion not in self.__extantions):
            raise Exception("extantion must be in {}".format(str(self.__extantions)))
        else:
            # auto read by extention
            self.__data = self.__read()
    def get_data(self):
        return self.__data
    def get_extantion(self):
        return self.__extantion
    def get_extantions(self):
        return self.__extantions
    def get_args(self):
        return self.__args
    def __read(self):
        match self.__extantion:
            case "csv":
                if(self.__args):
                    return pd.read_csv(self.__path,**self.__args)
                else:
                    return pd.read_csv(self.__path)
            case "json":
                if(self.__args):
                    return pd.read_json(self.__path,**self.__args)
                else:
                    return pd.read_json(self.__path)
            case "xlsx":
                if(self.__args):
                    return pd.read_excel(self.__path,**self.__args)
                else: 
                    return pd.read_excel(self.__path)
    # connect pandas data
    def connect(self,arr_data):
        return pd.concat([self.__data,*arr_data])
    # if columns arrgument is empty will return all values
    # in pandas data as list
    # else will take columns as pandas column
    def all_in_list(self,*columns):
        my_list = []
        if columns :
            try:
                for column in columns:
                    my_list += self.__data[column].values.tolist()
            except:
                print("key not exist")
        else: 
            for i in list(self.__data):
                my_list += self.__data[i].values.tolist()
        # remove empty values
        my_list = np.array(my_list)
        # remove empty elments
        return my_list[~pd.isnull(my_list)].tolist()
    def most_frequent(self,*columns):
        my_list = self.all_in_list(*columns)
        counts = np.bincount(my_list)
        return np.argmax(counts)
    
        # Python program to get average of a list 
    def average(self , *columns): 
        my_list = self.all_in_list(*columns)
        return np.average(my_list)