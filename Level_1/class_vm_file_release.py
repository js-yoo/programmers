 """
클래스 실습-자판기 완성하기(파일사용)

"""
import sys


# 가격은 100원 단위이므로 PRICE_UNIT 상수 값을 100으로 선언한다.
PRICE_UNIT = 100

class texts:
    title          = "#### 하나 %s 자판기 입니다. ####"
    product        = "%s:%s(%s원)"
    insert_coin    = "동전을 넣어 주세요. : "
    n_enough_coin  = "동전이 부족합니다.\n거스름돈은 %s원 입니다."
    select_product = "원하시는 상품번호를 선택하세요."
    select_fault   = "잘 못 누르셨습니다."
    product_out    = "선택하신 %s 입니다. 거스름돈은 %s원 입니다.\n감사합니다."

class Product:
    # 제품 종류, 가격을 코드변경없이 데이터를 쉽게 추가하거나 변경할 수 있다.
    productType = []
    productValue = []

           
class CoffeeVM(Product):
    _product_info_file = "coffee.txt"
    _name = "커피"
      
    def __init__(self):
       # 사용자가 자판기 종류를 선택하면 _name 출력한다.
       print( texts.title %self._name)
 
    def set_products(self):
        # 제품 종류, 가격 리스트를 초기화 한다. 
        Product.productType = []
        Product.productValue = []
        
        with open(self._product_info_file, "r", encoding="UTF-8") as fd:
            for line in fd:
                # 라인 끝에있는 \n를 제거하고 ,로 구분하는 리스트를 만든다.
                list = line.strip('\n').split(',')
                # 제품 종류, 가격 리스트에 필요한 값을 입력한다 
                Product.productType.append((list[0]+','+list[1]))
                Product.productValue.append((list[0]+','+list[2]))


    def run(self):

        self.set_products()

        while True:
           try:
               inputCoin = float(input(texts.insert_coin))
           except ValueError:
               # 잘못된 값을 입력받으면 에러 메시지를 출력한다.
               print(texts.select_fault)
           else:
               self.selectProduct(inputCoin)
               
                   
    def selectProduct(self, coin):
       # 제품 종류를 리스트로 선언하여 코드변경없이 데이터를 동적으로 보여준다.
       description = ''
       for line in Product.productType:
           list = line.split(',')
           # 제품 가격을 가져온다.
           price = self.getProductValue(list[0])
           description += list[0]+':'+list[1]+'('+str(price)+'원) '


       print(description)
       inputProduct = input( texts.select_product )
       productValue = self.getProductValue(inputProduct)

       # 입력한 값에 해당하는 내용이 리스트에 없으면 0이 반환된다.
       if productValue:
          productName = self.getProductName(inputProduct)
          self.payment(coin, productName, productValue)
       else:
          # 잘못된 값을 입력받으면 에러 메시지를 출력하고 제품선택 메뉴로 이동한다. 
          print(texts.select_fault)
          self.selectProduct(coin)


    def getProductValue(self, product):
        returnValue = 0
        for line in Product.productValue:
            list = line.split(',')
            if list[0] == product:
                returnValue = list[1]

        return int(returnValue)

    def getProductName(self, product):
        for line in Product.productType:
            list = line.split(',')
            if list[0] == product:
                return list[1]

    def payment(self, coin, name, value):
        coinValue = coin * PRICE_UNIT
        if coinValue >= value:
           balance = coinValue - value
           print(texts.product_out %(name ,int(balance)))
        else:
           print(texts.n_enough_coin %int(coinValue))
        # 지불을 마치면 초기 메뉴로 이동한다.           
        self.run()


#과자 클래스는 커피 클래스를 상속받는다  
class SnackVM(CoffeeVM):
    _product_info_file = "snack.txt"
    _name = "과자"
 

################################################################################

if __name__ == '__main__':

    print("1:커피, 2:과자")
    select_vm = input("구동할 자판기를 선택하세요.").strip()
    
    if select_vm == "1":
        vm = CoffeeVM()
    
    elif select_vm == "2":
        vm = SnackVM()
    
    else:
        print("잘 못 누르셨습니다. 다시 실행 해 주세요.")
        sys.exit(-1)

    try:
        vm.run()

    except KeyboardInterrupt as exc:
        print("판매를 종료합니다.")
