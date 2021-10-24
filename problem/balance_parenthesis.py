def parenthesis(exp):
    st=[]
    c=0
    for ch in exp:
        if ch in ['(','{','['] :
            st.append(ch)
        else:
            if not st:
                return False
            curr=st.pop()
            if curr=='(':
                if ch!=')':
                    return False
            if curr=='{':
                if ch!='}':
                    return False
            if curr=='[':
                if ch!=']':
                    return False
            
    if st:
        return False
    return True

expr = "{()}[]"

if parenthesis(expr):
    print('Balanced Parenthesis')
else:
    print('Not Balanced Parenthesis')
        