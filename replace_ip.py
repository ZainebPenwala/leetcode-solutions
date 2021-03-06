'''Given a valid (IPv4) IP address, return a defanged version of that IP address. A defanged IP address replaces every period "." with "[.]".
Example 1:
Input: address = "1.1.1.1"          Output: "1[.]1[.]1[.]1"
Example 2:
Input: address = "255.100.50.0"     Output: "255[.]100[.]50[.]0" '''


# Solution 1: without using .replace() 
class Defang:
    def defang(self, ip):
        ans = ''
        for x in ip:
            if x == '.':
                x = '[' + '.' +']'
            ans +=x
        return ans

obj = Defang()
obj.defang('1.1.1.1')


# Solution 2:using .replace()
class Replace:
    def replace(self, ip):
        r = ip.replace('.', '[.]')
        return r
        

obj = Replace()
obj.replace('1.1.1.1')
