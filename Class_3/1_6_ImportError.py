#import error will occur when you are tyring to import a module which is not present in the system 
#there are two types of import errors 
#one is the python is unable to found a module "ModueleNotFoundError"
#second one is python is able to find the module, but it does not contain the definition you are importing "ImportError"

import dabba #This will throw ModuleNotFound error

from numpy import dabba #This will throw ImportError