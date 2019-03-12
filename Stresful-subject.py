'''
The function should recognise if a subject line is stressful. 
A stressful subject line means that all letters are in uppercase, 
and/or ends by at least 3 exclamation marks, 
and/or contains at least one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.

Output: Boolean.

Precondition: Subject can be up to 100 letters
'''
import re;
def is_stressful(subj):
    """
        recoognise stressful subject
        up to 100 letters
    """
    subj = str(subj);
    if (len(subj) > 100 or
        subj.isupper() == True or
        len(re.findall('.!!!$', subj)) == 1):
            return True
            
    mssg = re.sub(r'[^\w]', '', subj);
    mssg = mssg.lower();
    if( len(re.findall('[h]+[e]+[l]+[p]+', mssg)) >= 1 or
        len(re.findall('([u]+[r]+[g]+[e]+[n]+[t]+)', mssg)) >= 1 or
        len(re.findall('([a]+[s]+[a]+[p]+)', mssg)) >= 1):
            return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
