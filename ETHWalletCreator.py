from pywallet import wallet

class CreateWallet(object):
    def __init__(self, name, seed, children ):
        if (seed == "0"):
            self.seed = wallet.generate_mnemonic()
        else:
            self.seed = seed

        self.name = name
        self.children = children
        self.wallet = wallet.create_wallet(network="ETH", seed=self.seed, children=self.children)
        self.wallet_data = dict(self.wallet)


    def addresses(self):
        addresses = ""
        for item in self.wallet_data['children']:
            addresses += item['address']+"\n"
        return addresses.rstrip()

    def admin_data(self):
        data = ""
        data +=f'''
=========================================================================================
wallet name       = {self.name}
coin              = ETH
seed              = {self.seed}
private_key       = {self.wallet_data['private_key'].encode()}
public_key        = {self.wallet_data['public_key'].encode()}
xprivate_key      = {self.wallet_data['xprivate_key']}
xpublic_key       = {self.wallet_data['xpublic_key']}
address           = {self.wallet_data['address'].encode()}
xpublic_key_prime = {self.wallet_data['xpublic_key_prime']}
children          =
'''+self.addresses()+'''
=========================================================================================
'''
        return data

        

if __name__ == "__main__":
    print('''
    welcome , the duty of this scrypt is create etherume wallet with multiple address(HD Wallet)
    also you can restore your addresses with seed
    ''')

    name = input("wallet name : ")
    print("seed (input space in between each word) (!!! if you wana scrypt create seed input number '0' ")
    seed = input(": ")
    children = int(input("how many address you need : "))
    my_wallet = CreateWallet(name, seed, children)
    print("\n### wallet created ###\n")

    first_file_name = input("name for exporting addresses : ")+".txt"
    second_file_name= input("name for exporting admin data: ")+".txt"

    f1 = open(first_file_name,"a")
    f1.write(my_wallet.addresses())
    f1.close()

    f2 = open(second_file_name,"a")
    f2.write(my_wallet.admin_data())
    f2.close()
    print("done")
