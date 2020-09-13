import pandas as pd
from .split import split

class Crypto:
    def __init__(self) -> None:
        self.encryptionkey = pd.read_csv(r"./assets/decodekeynew.csv", sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])
        self.df = pd.DataFrame(data=self.encryptionkey)
        self.df['Character'] = self.df['Character'].astype(str)
        self.df['Byte'] = self.df['Byte'].astype(str)
    
    def encrypt(self, msg: str) -> str:
        splited_msg = split(msg)
        cipher_text = ""
        for i in range(len(splited_msg)):
            coded_char = ""
            j = splited_msg[i]
            try:
                coded_char = self.encryptionkey.loc[self.encryptionkey['Character'] == j, 'Byte'].iloc[0]
            except:
                print('unrecognized character')
                coded_char = '@@@'
            cipher_text += coded_char
        return cipher_text

    def decrypt(self, cipher_text: str) -> str:
        plain_text = ""
        new_word = []
        for i in range(0, len(cipher_text), 2):
            j = cipher_text[i:i + 2]
            index_nb = self.df[self.df.eq(j).any(1)]
            df = index_nb['Character'].tolist()
            s = [str(x) for x in df]
            new_word += s
        plain_text = ''.join(new_word)
        return plain_text
