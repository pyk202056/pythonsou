class ElecProduct:
    volume = 0

    def volumeControl(self, volume):
        # print(f'볼륨을 조절한다 : {volume}')
        pass


class ElecTv(ElecProduct):
    def tv1(self):
        print('ElecTv 고유 메소드')

    def volumeControl(self, volume):
        # 계산 ...
        print('금요일 와우')
        self.volume = volume
        print(f'ElecTv 볼륨을 조절한다 : {volume}')

class ElecRadio(ElecProduct):
    def volumeControl(self, volume): 
        sori = volume
        print(f'ElecRadio 소리를 조절 : {sori}')

product = ElecProduct()
tv = ElecTv()
product = tv
product.volumeControl(5)
print()
radio = ElecRadio()
product = radio
product.volumeControl(3)

print('-------')
q1 = [ElecTv(), ElecRadio()]
for a in q1:
    a.volumeControl(2)
    print()
