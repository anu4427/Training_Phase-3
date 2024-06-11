def travel(src,dest,result=[]):
    for i in range(len(src)):
        if src[i]=='abc' and dest[i]=='klo':
            result.append('c')
        elif (src[i]=='abc' or src[i]=='klo')and (dest[i]=='ijk' or dest[i]=='cde'):
            result.append('bc')
        elif (src[i]=='abc' or src[i]=='klo')and (dest[i]=='efg'or dest[i]=='ghi'):
            result.append('abc')
        elif src[i]=='cde' and dest[i]=='ijk':
            result.append('b')
        elif (src[i]=='cde' or src[i]=='ijk')and (dest[i]=='klo' or dest[i]=='abc'):
            result.append('bc')
        elif (src[i]=='cde'or src[i]=='ijk') and (dest[i]=='efg' or dest[i]=='ghi'):
            result.append('ab')
        elif src[i]=='efg' and dest[i]=='ghi':
            result.append('a')
        elif (src[i]=='efg'or src[i]=='ghi')and(dest[i]=='ijk'or dest[i]=='cde'):
            result.append('ab')
        else:
            result.append('abc')
    return result

        
src=['abc','efg','efg']
dest=['klo','ijk','klo']
print(travel(src,dest))
