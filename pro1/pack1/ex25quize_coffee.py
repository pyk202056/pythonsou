class CoinIn:
    def __init__(self):
        self.cupPrice = 200

    def calc(self, coin, cupCount):
        totalPrice = self.cupPrice*cupCount

        if coin < totalPrice:
            return None, None
        else:
            change = coin - totalPrice
            return cupCount, change


class MachineUI:
    def __init__(self):
        self.coinIn = CoinIn()

    def showData(self):
        coin = int(input('동전을 입력하세요 : '))
        cup = int(input('몇 잔을 원하세요 : '))

        cupCount, change = self.coinIn.calc(coin, cup)

        if cupCount is None:
            print('요금이 부족합니다.')
        else:
            print(f'커피 {cupCount}잔과 잔돈 {change}원')

if __name__ == "__main__":
    ui = MachineUI()
    ui.showData()