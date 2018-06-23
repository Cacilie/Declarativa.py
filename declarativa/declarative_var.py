import copy

class declarative_var: 
    
    def __init__(self, type_var, variable):
        if type(variable) is type_var:
            self.var_value = variable
            self.type_var = type_var
            self.prevState =  None
        else:
            message = str(variable) + " is not a " + str(type_var)
            raise Exception(message)
    
    def get(self):
        return self.type_var(copy.copy(self.var_value))

    def set(self, var_value):
        if type(var_value) is self.type_var:
            self.prevState = self.var_value
            self.var_value = var_value
        else:
            message = str(var_value) + " is not a " + str(self.type_var)
            raise Exception(message)
    
    def getPrevState(self):
        if self.prevState != None:
            return self.type_var(copy.copy(self.prevState))
        else:
            return None