def validate_brackets(str):
    list_str=list(str)
    brackets=['{','[','(']
    temp=[]

    for item in list_str:
        if item in brackets:
            temp+=[item]
        else:
            popped_val= temp.pop()
            if  popped_val== '(':
                if item != ")":
                    return False
            if popped_val == '{':
                if item != "}":
                    return False
            if popped_val == '[':
                if item != "]":
                    return False
            if temp:
                return False
            else:
                return True
