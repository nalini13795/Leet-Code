'''
Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]

'''

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if(len(strs)):
            return chr(257).join(strs)
        else:
            chr(258)
                
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if(s == chr(258)):
            return [""]
        else:
            return s.split(chr(257))
        
